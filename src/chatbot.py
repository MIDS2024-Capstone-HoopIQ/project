import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import datetime

# Load the FAISS index and dataframe
index = faiss.read_index('../data/vector_store.index')
df = pd.read_csv('../data/wnba_pbp_2018.csv')

# Load the model for encoding
model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to process the query and return results
def query_data(query):
    # Convert the query to an embedding
    query_embedding = model.encode([query])

    # Search the FAISS index
    D, I = index.search(query_embedding, k=10)  # Adjust k as needed

    # Retrieve the rows corresponding to the indices
    result_rows = df.iloc[I[0]].to_dict(orient='records')

    return result_rows

# Streamlit application
st.title("WNBA Data Chatbot")
st.write("Ask a question about the WNBA data:")

query = st.text_input("Your question:", "")

if query:
    result_rows = query_data(query)

    st.write(f"Results for: '{query}'")
    
    if result_rows:
        for index, row in enumerate(result_rows):
            st.write(f"**Index:** {row['id']}")
            st.write(f"**Type:** {row['type_text']}")
            st.write(f"**Description:** {row['text']}")
            st.write(f"**Away Score:** {row['away_score']}")
            st.write(f"**Home Score:** {row['home_score']}")
            st.write(f"**Period:** {row['period_display_value']}")
            st.write(f"**Clock:** {row['clock_display_value']}")
            st.write("\n")
    else:
        st.write("No results found.")