from tavily import TavilyClient
from langchain.tools import tool


tavily_client = TavilyClient()


@tool
def tavily_search(user_question: str):
    """Search the web using Tavily and return the top 6 relevant results."""

    response = tavily_client.search(
        query=user_question,
        max_results=6,
        search_depth="advanced",
    )

    return response