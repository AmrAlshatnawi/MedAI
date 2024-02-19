import streamlit as st
from streamlit.logger import get_logger
from langchain.chains import LLMChain
from langchain.llms import openai
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory
from langchain.prompts import PromptTemplate 
from openai import OpenAI

LOGGER = get_logger(__name__)
st.set_page_config(
        page_title="MedAI",
        page_icon="🤖",
    )

st.title("🤖MedAI")

    

# Read OpenAI API key
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
# Check if key was retrieved 
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")


st.header("""🌟 Welcome to Our Web Application – Your Gateway to Informed Health Decisions! 🌟

""")