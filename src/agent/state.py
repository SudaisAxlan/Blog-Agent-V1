from typing import TypedDict


class AgentState(TypedDict):
    user_title: str
    google_search: list[str]
    raw_content: str
    formatted_content: str
    final_content: str