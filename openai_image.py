import os 
import base64
from obtain_key import getkey
from openai import OpenAI

key=getkey('OPENAI_API_KEY')
client=OpenAI(api_key=key)

prompt='A futuristic cityspace with flying cars at sunset'

link=client.images.generate(
    model='gpt-images-2',
    prompt=prompt,
    #size="1024x1024"
)

image_base64=link.data[0].b64_json
image_bytes=base64.b64decode(image_base64)

with open("futuristic_city.png", "wb") as f:
    f.write(image_bytes)

