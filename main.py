import streamlit as st
from dotenv import load_dotenv

from utils import get_prompts, set_sidebar
from crud import download_prompts

load_dotenv()

st.set_page_config(
    page_title='Repods AI',
    layout='wide',
    initial_sidebar_state='expanded'
)

download_prompts()

prompts = get_prompts()

st.title("Repods AI")


set_sidebar()

# st.switch_page('pages/1_page1.py')
