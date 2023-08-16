#integrate code with open api
import os
from constants import openai_key
from langchain.llms import OpenAI
import streamlit as st

os.environ['OPENAI_API_KEY'] = openai_key
# initializing streamlit framework

st.title('Language Chain OpenAI Demo')

input_text = st.text_input('Search Topic', 'Enter your topic here')

#Openai llms
llms = OpenAI(temperature=0.8)

if input_text:
    st.write(llms(input_text))
