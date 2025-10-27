from langchain_groq import ChatGroq
from tools.conversion_tools import get_conversion_factor, convert
from dotenv import load_dotenv
import os

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(groq_api_key=groq_api_key, model="llama-3.1-8b-instant")

llm_with_tools = llm.bind_tools([get_conversion_factor, convert])