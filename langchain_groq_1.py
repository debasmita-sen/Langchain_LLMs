import os 
from langchain_groq import ChatGroq
from obtain_key import getkey

key=getkey("GROQ_API_KEY")


llm=ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
)
response=llm.invoke("What is ML")
print(response.content)
