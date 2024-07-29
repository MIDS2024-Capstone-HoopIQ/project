import streamlit as st
import pandas as pd
import datetime
from wnba_langchain import get_response
from about import about

# Define navigation function
def navigate_to(page):
    st.session_state.current_page = page
    
# Define page content
def home():
	st.title("HoopsIQ - WNBA")
	st.write("Ask a question about WNBA data:")
	st.markdown(
		"""
		<style>
		.big-divider {
			height: 5px;
			background-color: #333;
			margin: 20px 0;
		}
		</style>
		<div class="big-divider"></div>
		""",
		unsafe_allow_html=True
	)

	if 'responses' not in st.session_state:
		st.session_state.responses = []
	
	def handle_query():
		query = st.session_state.query
		if query:
			langchain_response = get_response(query)
			streamlit_response = f"<b>Question:</b>\n\n{query}\n\n\n<b>Response:</b>\n\n{langchain_response}"
			st.session_state.responses.append(streamlit_response)
			st.session_state.query = ""
			
	st.text_input("Your question:", key='query', on_change=handle_query)

	for response in reversed(st.session_state.responses):
		st.markdown("---")
		st.markdown(response, unsafe_allow_html=True)

# Initialize session state for page navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Home'

# Navigation links
st.sidebar.title("Navigation")
st.sidebar.button("Home", on_click=lambda: navigate_to("Home"))
st.sidebar.button("About", on_click=lambda: navigate_to("About"))

# Render the appropriate page content
if st.session_state.current_page == "Home":
    home()
elif st.session_state.current_page == "About":
    about()
