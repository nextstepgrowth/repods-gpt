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
        st.title('Page')
        st.logo(image='logo.svg', size='medium', link='https://repods-gpt.streamlit.app/')
        st.page_link('pages/1_page1.py', label='배터리, 칩셋 검수')
        st.page_link('pages/2_page2.py', label='케이스 상태 검수')
        st.page_link('pages/3_page3.py', label='레이블 정확도 검수')
        st.page_link('pages/4_page4.py', label='공정 파라미터 검수')
        # st.page_link('pages/5_admin.py', label='Admin')

def get_prompts():
    prompts = []
    for i in range(1, 5):
        with open(f'prompts/prompt-page{i}.txt', 'r') as f:
            prompt = f.read()
            prompts.append(prompt)
    return prompts
