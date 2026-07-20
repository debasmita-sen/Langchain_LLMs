import os 
from obtain_key import getkey
from openai import OpenAI

key=getkey('OPENAI_API_KEY')
client=OpenAI(api_key=key)

def summarize(data):
    response=client.chat.completions.create(
        model='gpt-5.4',
        messages=[
            {"role":"system","content":"You are a summarizer"},
            {"role":"user","content":f"Summarize this text in 3 lines:\n{data}"}
        ]
    )
    return response.choices[0].message.content

text='''
Artificial intelligence (AI) is the capability of computational systems to perform tasks typically associated with human intelligence, such as learning, reasoning, problem-solving, perception, and decision-making. It is a field of research in engineering, mathematics, and computer science that develops and studies methods and software that enable machines to perceive their environment and use learning and intelligence to take actions that maximize their chances of achieving defined goals.[1]

High-profile applications of AI include advanced web search engines, chatbots, virtual assistants, autonomous vehicles, and play and analysis in strategy games (e.g., chess and Go). Since the 2020s, generative AI has become widely available to generate images, audio, and videos from text prompts.

The traditional goals of AI research include learning, reasoning, knowledge representation, planning, natural language processing, and perception, as well as support for robotics.[a] To reach these goals, AI researchers use techniques including state space search and mathematical optimization, formal logic, artificial neural networks, and methods based on statistics, operations research, and economics.[b] AI also draws upon psychology, linguistics, philosophy, neuroscience, and other fields.[2] Some companies, such as OpenAI, Google DeepMind, and Meta, aim to create artificial general intelligence (AGI)—AI that can complete nearly any cognitive task at least as well as a human.[3]


'''

print(summarize(text))
