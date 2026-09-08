import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not set in your .env file")

llm = ChatGroq(
    model="openai/gpt-oss-20b",         
    # model="openai/gpt-oss-120b",      
   
    api_key=api_key,
    temperature=0.7
)







# import os

# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI


# load_dotenv()


# api_key = os.getenv("GEMINI_API_KEY")

# if not api_key:
#     raise ValueError(
#         "GEMINI_API_KEY is not set. Please add it to your .env file."
#     )


# llm = ChatGoogleGenerativeAI(
#     model="gemini-3.1-flash-lite-preview",
#     api_key=api_key,
#     temperature=0.2,
# )