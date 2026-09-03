from langchain_xai import ChatXAI


llm = ChatXAI(
    model="grok-4.6",
    temperature=0.2,
)