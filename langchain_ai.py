import os 
from langchain_openai import ChatOpenAI
from obtain_key import getkey

key = getkey("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=key
)

response = llm.invoke("What is machine learning?")
print(response.content)
