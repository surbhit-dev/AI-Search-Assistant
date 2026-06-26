import google.generativeai as genai

from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_response(query, results):

    if not results:
        return "No relevant information found."

    context = ""

    for item in results[:3]:

        context += f"""
Title: {item['title']}

Content:
{item['chunk']}

"""

    prompt = f"""
User Question:
{query}

Web Information:
{context}

Instructions:
1. Answer the user's question.
2. Use only the provided information.
3. If the answer is not present, say so.
4. Be factual and concise.
5. Do not invent information.
"""

    response = model.generate_content(prompt)

    return response.text