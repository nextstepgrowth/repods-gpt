import os
import streamlit as st
from langchain_openai import ChatOpenAI


openai_api_key = os.getenv('OPENAI_API_KEY')

def get_chat_response(input):
    model = ChatOpenAI(api_key=openai_api_key, model='gpt-4o')
    response = model.invoke(input=input)
    return response.content

def set_sidebar():
    with st.sidebar:
        st.title('사이드바')
        st.page_link('pages/1_page1.py', label='Page 1')
        st.page_link('pages/2_page2.py', label='Page 2')
        st.page_link('pages/3_page3.py', label='Page 3')
        st.page_link('pages/4_admin.py', label='Admin')

def get_prompts():
    prompts = []
    for i in range(1, 4):
        with open(f'prompts/prompt-page{i}.txt', 'r') as f:
            prompt = f.read()
            prompts.append(prompt)
    return prompts
