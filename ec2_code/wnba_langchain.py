import boto3
import os
import requests
from langchain.agents import AgentExecutor
from langchain.agents import tool
from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.chat_message_histories import (
    DynamoDBChatMessageHistory,
)
from langchain_community.utilities import SQLDatabase
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain.globals import set_debug
from langchain_openai import ChatOpenAI
from sqlalchemy import create_engine
from urllib.parse import quote_plus

AWS_REGION = "us-east-1" # Change me
SCHEMA_NAME = "wnba_db" # Athena calls this a database
S3_STAGING_DIR = "s3://wnbadata/" # Change me

dynamodb = boto3.resource("dynamodb")

connect_str = "awsathena+rest://athena.{region_name}.amazonaws.com:443/{schema_name}?s3_staging_dir={s3_staging_dir}"

engine = create_engine(connect_str.format(
        region_name=AWS_REGION,
        schema_name=SCHEMA_NAME,
        s3_staging_dir=quote_plus(S3_STAGING_DIR)
))

db = SQLDatabase(engine)
schema = db.get_table_info()

os.environ["OPENAI_API_KEY"] = "sk-proj-Jz56EPt2tMFrDJtB1Q2dT3BlbkFJBOkimFUK14hExlzvsvJF"

llm = ChatOpenAI( model_name= "gpt-4", temperature= 0)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
tools = toolkit.get_tools()
llm_with_tools = llm.bind_tools(tools)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are an agent designed to interact with a SQL database.
        Given an input question, create a syntactically correct SQLite query to run, then look at the results of the query and return the answer.
        Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most 5 results.
        You can order the results by a relevant column to return the most interesting examples in the database.
        Never query for all the columns from a specific table, only ask for the relevant columns given the question.
        You have access to tools for interacting with the database.
        Only use the below tools. Only use the information returned by the below tools to construct your final answer.
        You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.
        
        DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.
        
        To start you should ALWAYS look at the tables in the database to see what you can query.
        Do NOT skip this step.
        Then you should query the schema of the most relevant tables.""",
    ),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_to_openai_tool_messages(
            x["intermediate_steps"]
        ),
        "chat_history": lambda x: x["chat_history"],
    }
    | prompt
    | llm_with_tools
    | OpenAIToolsAgentOutputParser()
)
agent_executor = AgentExecutor(agent = agent, tools = tools, verbose = False, return_intermediate_steps = True)

my_key = {
    "SessionId": "session_id::0",
    "UserID": "0001",
}

chat_history = DynamoDBChatMessageHistory(
    table_name="Chat_Table",
    session_id="0",
    key=my_key,
)

def get_response(input_text):
	if input_text:
		response = agent_executor.invoke({
			'input': input_text,
			'chat_history': chat_history.messages,
		})
		chat_history.add_user_message(input_text)
		chat_history.add_ai_message(response["output"])
		return response['output']
