from ingestion.pdf_reader import read_pdf

from graph.graph_builder import build_graph

def main():
    file_path = "Sample.pdf"  # Replace with your PDF file path
    text = read_pdf(file_path)
    graph = build_graph()
    result = graph.invoke({"text": text})
    print("Final Summary:\n", result["summary"])

if __name__ == "__main__":    
    main()








# from processing.chunking import chunk_text     
# from Summarizer.summarize import summarize_chunks 
# from config import get_llm


# if __name__ == "__main__":
#     file_path = "Sample.pdf"  # Replace with your PDF file path
#     text = read_pdf(file_path)
#     print(text)
#     chunks = chunk_text(text)
#     for i, chunk in enumerate(chunks):
#         print(f"Chunk {i + 1}:\n{chunk}\n") 

#     summaries = summarize_chunks(chunks)
#     # 
#     print("Final Summary:\n", summaries)



    


        