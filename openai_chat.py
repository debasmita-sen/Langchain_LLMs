import os 
from obtain_key import getkey
from openai import OpenAI

key=getkey('OPENAI_API_KEY')
client=OpenAI(api_key=key)
ask=input('\nEnter the question -')
response=client.responses.create(
    model='gpt-5.4',
    max_output_tokens=300,
    temperature=1,
    input=ask,
    reasoning={"effort":"medium"}
)
print(response.output_text)