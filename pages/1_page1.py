import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import streamlit as st
import base64

from utils import get_chat_response, get_prompts, set_sidebar

set_sidebar()

img_files = []
img_datas = []
response = ''
prompts = get_prompts()

with st.container(height=750, border=False): 
    img_files = st.file_uploader('File uploader', accept_multiple_files=True, type=['jpg', 'png', 'jpeg'])
    col1, col2, col3 = st.columns(3)
    with col1:
        if len(img_files) > 0:
            st.image(img_files[0], caption='Uploaded image', use_container_width=True)
            img_datas.append(base64.b64encode(img_files[0].read()).decode('utf-8'))
        else:
            st.container(height=200)

    with col2:
        if len(img_files) > 1:
            st.image(img_files[1], caption='Uploaded image', use_container_width=True)
            img_datas.append(base64.b64encode(img_files[1].read()).decode('utf-8'))
        else:
            st.container(height=200)

    with col3:
        if len(img_files) > 2:
            st.image(img_files[2], caption='Uploaded image', use_container_width=True)
            img_datas.append(base64.b64encode(img_files[2].read()).decode('utf-8'))
        else:
            st.container(height=200)

    if st.button('제출'):
        content = []
        content.append({'type': 'text', 'text': prompts[0]})
        for i in range(len(img_files)):
            content.append({'type': 'image_url', 'image_url': {'url': f'data:{img_files[i].type};base64,{img_datas[i]}'}})

        response = get_chat_response([HumanMessage(content=content)])

    
    st.text_area('결과', value=response, height=100, disabled=True)