from processing.chunking import chunk_text
from Summarizer.summarize import summarize_chunks

def chunk_node(state):
    text = state['text']
    chunks = chunk_text(text)
    
    return {"chunks": chunks}

def summarize_node(state):
    chunks = state['chunks']
    summary = summarize_chunks(chunks)
    
    return {"summary": summary}

