import os 
from obtain_key import getkey
from openai import OpenAI

key=getkey('OPENAI_API_KEY')
client=OpenAI(api_key=key)

def comment(code):
    response=client.chat.completions.create(
        model='gpt-5.4',
        messages=[
            {"role":"system","content":"You are a python code reviewer"},
            {"role":"user","content":f"Add meaningful inline comments to this code:\n{code}"}
        ]
    )
    return response.choices[0].message.content

code='''
import math
def factorial(n):
    if n==0
        return 1
    else
        return n*math.factorial(n-1)
'''

print(comment(code))