
import streamlit as st
from langchain_core.messages import HumanMessage

from utils import get_chat_response, get_prompts, set_sidebar

set_sidebar()

img_files = []
img_datas = []
response = ''
prompts = get_prompts()

with st.container(height=750, border=False): 
    st.container(height=300, border=False)
    
    input_text = st.text_area('Enter text here')


    if st.button('제출'):
        content = []
        content.append({'type': 'text', 'text': prompts[3]})
        content.append({'type': 'text', 'text': input_text})
        response = get_chat_response([HumanMessage(content=content)])

    st.text_area('결과', value=response, height=300, disabled=True)

