from src.agent.state import AgentState
from src.tests.web_search import tavily_search

def search_node(state: AgentState) -> dict:
    user_title = state["user_title"]

    search_results = tavily_search.invoke({
        "user_question": user_title
    })

    return {
        "google_search": search_results
    }