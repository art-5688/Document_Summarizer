from langgraph.graph import StateGraph
from graph.state import Graph_state
from graph.nodes import chunk_node, summarize_node


def build_graph():
    builder = StateGraph(Graph_state)
    
    builder.add_node("chunk_node", chunk_node)
    builder.add_node("summarize_node", summarize_node)

    builder.set_entry_point("chunk_node")

    builder.add_edge("chunk_node", "summarize_node")

    return builder.compile()
