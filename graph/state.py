from typing import TypedDict, List

class Graph_state(TypedDict):
    text: str
    chunks: List[str]
    summary: str

    