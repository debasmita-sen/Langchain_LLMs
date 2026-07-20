#Resume skill extractor

import os 
from obtain_key import getkey
from openai import OpenAI

key=getkey('OPENAI_API_KEY')
client=OpenAI(api_key=key)

def extract_skills(resume_text):
    response=client.chat.completions.create(
        model='gpt-5.4',
        messages=[
            {"role":"system","content":"You can extract technical and soft skills"},
            {"role":"user","content":f"Extract all skills from this resume:\n{resume_text}"}
        ]
    )
    return response.choices[0].message.content

resume_text='''
We are looking for a skilled Software Developer with expertise in Python, AI/ML, Java, and Spring Boot.
The role involves developing machine learning solutions, REST APIs, and scalable backend applications.
Required skills include Python, Pandas, NumPy, Scikit-learn, SQL, Java, Spring Boot, and Git.
Knowledge of model training, data preprocessing, API integration, and database management is essential.
Candidates should have strong problem-solving skills and experience working on end-to-end software projects.

'''

print(extract_skills(resume_text))