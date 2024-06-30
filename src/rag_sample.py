import boto3
import pandas as pd
from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration
import torch

bucket_name = 'wnbadata'
file_key = 'player-info/player-info.csv'
s3 = boto3.resource('s3')

obj = s3.Object(bucket_name, file_key)
data = obj.get()['Body'].read().decode('utf-8')

df = pd.read_csv(pd.compat.StringIO(data))
df['combined_context'] = df['athlete_name'].astype(str) + " " + df['athlete_birthdate'].astype(str) + " " + df['athlete_college'].astype(str)
documents = df['combined_context'].tolist()

tokenizer = RagTokenizer.from_pretrained('facebook/rag-sequence-nq')
retriever = RagRetriever.from_pretrained(
    'facebook/rag-sequence-nq',
    index_name="custom",
    passages=documents
)

model = RagSequenceForGeneration.from_pretrained('facebook/rag-sequence-nq', retriever=retriever)

def generate_response(question, model, tokenizer):
    inputs = tokenizer(question, return_tensors='pt')
    with torch.no_grad():
        outputs = model.generate(input_ids=inputs['input_ids'])
    return tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]

question = "What is the combined information from column1, column2, and text of the first document?"

# Generate response
response = generate_response(question, model, tokenizer)
print(f'Response: {response}')
