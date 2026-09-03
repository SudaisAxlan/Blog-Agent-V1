from langgraph.graph import StateGraph, START, END

from src.agent.state import AgentState

from src.agent.nodes.search_node import search_node
from src.agent.nodes.raw_content_node import raw_content_node
from src.agent.nodes.formet_node import format_node
# from src.agent.nodes.writing_node import writing_node
# from src.agent.nodes.format_node import format_node
from src.agent.nodes.final_content_node import final_content_node


# Create graph
graph = StateGraph(AgentState)


# ========================
# NODES
# ========================

graph.add_node("search_node", search_node)
graph.add_node("writing_node", raw_content_node)
graph.add_node("format_node", format_node)
graph.add_node("final_content_node", final_content_node)


# ========================
# EDGES
# ========================

graph.add_edge(START, "search_node")

graph.add_edge("search_node", "writing_node")

graph.add_edge("writing_node", "format_node")

graph.add_edge("format_node", "final_content_node")

graph.add_edge("final_content_node", END)


# ========================
# COMPILE GRAPH
# ========================

blog_agent = graph.compile()
