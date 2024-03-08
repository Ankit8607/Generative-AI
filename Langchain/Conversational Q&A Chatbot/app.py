# Q&A Chatbot
from langchain_openai.llms import OpenAI
import streamlit as st


# Function to load OpenAI model and get response 

def get_openai_response(question):
    llm=OpenAI(openai_api_key='sk-A7EYUoz0X44JD29iPblAmH4hRF2l1zZ2', temperature=0.7)
    response=llm(question)
    return response


# create our UI using streamlit

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain application")

input=st.text_input("Input: ",key='input')
response = get_openai_response(input)

submit = st.button("Ask the question")

# If ask button is clicked

if submit:
    st.subheader("The response is")
    st.write(response)