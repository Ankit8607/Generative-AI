## Integrate our code OpenAI API
import os
from constants import openai_key
from langchain_openai.llms import OpenAI
from langchain_core.prompts import ChatPromptTemplate

import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

# streamlit framework

st.title('Celebrity Search Results')
input_text=st.text_input("Search the topic u want")

# Prompt Template 
prompt = ChatPromptTemplate.from_template("tell me about celebrity {topic}")
prompt_value = prompt.invoke({"topic": input_text})

## OPENAI LLMS
llm=OpenAI(temperature=0.8)

if input_text:
    st.write(llm.invoke(prompt_value))
