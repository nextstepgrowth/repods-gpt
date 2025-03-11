
import streamlit as st

from utils import get_prompts, set_sidebar
from crud import upload_prompts

set_sidebar()

prompts = get_prompts()
options = ['page1', 'page2', 'page3']

option = st.selectbox('Select option', options)
if option == 'page1':
    st.session_state['text_area'] = st.text_area('Prompt', height=100, value=prompts[0])
elif option == 'page2':
    st.session_state['text_area'] = st.text_area('Prompt', height=100, value=prompts[1])
elif option == 'page3':
    st.session_state['text_area'] = st.text_area('Prompt', height=100, value=prompts[2])


if st.button("저장"):
    with open(f'./prompts/prompt-{option}.txt', 'w') as f:
        f.write(st.session_state['text_area'])
    upload_prompts()
    st.write('저장되었습니다.')
