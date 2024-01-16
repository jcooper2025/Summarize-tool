# code take from a demo video on the Certified Fresh Events youtube channel
# Streamlit 101: an intro to building web apps with just Python

import openai
import streamlit as st
from streamlit_chat import message
from streamlit_extras.color_header import color_header

openai.api_key = st.secrets["openai_apikey"]
st.set_page_config(page_title='Chat with GPT3 using Streamlit')
