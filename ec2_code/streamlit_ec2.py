import streamlit as st
import pandas as pd
import datetime
from wnba_langchain import get_response

st.title("WNBA Data Chatbot")
st.write("Ask a question about the WNBA data:")

if 'responses' not in st.session_state:
    st.session_state.responses = []

def handle_query():
    query = st.session_state.query
    if query:
        langchain_response = get_response(query)
        streamlit_response = f"Question:\n\n{query}\n\n\nResponse:\n\n{langchain_response}"
        st.session_state.responses.append(streamlit_response)
        st.session_state.query = ""
		
st.text_input("Your question:", key='query', on_change=handle_query)

for response in st.session_state.responses:
    st.write(response)
