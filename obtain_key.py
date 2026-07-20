import os
from openai import OpenAI
from dotenv import find_dotenv,load_dotenv

def getkey(s:str):
    '''
    This function is a key supplier
    '''
    load_dotenv(find_dotenv(),override=True)
    return os.getenv(s)



