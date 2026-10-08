from config import get_llm

def summarize_chunks(chunks):
    llm = get_llm()

    summaries = []

    # 🔹 Step 1: Summarize each chunk
    for chunk in chunks:
        prompt = f"""
        Summarize the following text in simple and clear language in 10 lines only:

        {chunk}
        """

        response = llm.invoke(prompt)
        summaries.append(response.content)

    # 🔹 Step 2: Combine summaries
    final_summary = "\n".join(summaries)

    return final_summary