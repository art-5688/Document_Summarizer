from config import get_llm

llm = get_llm()

response = llm.invoke("Explain AI in 2 lines")

print(response.content)