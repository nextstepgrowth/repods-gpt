import streamlit as st
from dotenv import load_dotenv

from utils import get_prompts, set_sidebar
from crud import download_prompts

load_dotenv()

download_prompts()

prompts = get_prompts()


st.switch_page('pages/1_page1.py')
