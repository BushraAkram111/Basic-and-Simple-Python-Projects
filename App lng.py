import streamlit as st
from langchain.chains import llm
from langchain import llms
from langchain.llms.base import LLM

st.title('Quickstart App')
openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    return llm(input_text, do_censor=True)

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')

    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!')

    if submitted and openai_api_key.startswith('sk-'):
        response = generate_response(text)
        st.write(response)