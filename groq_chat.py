import os
from groq import Groq
from obtain_key import getkey

key=getkey('GROQ_API_KEY')

client = Groq(api_key=key)

# 2. Start an empty message list for the conversation
messages = [
    {
        "role": "system",
        "content": "You are a helpful and friendly chatbot assistant."
    }
]

print("Chatbot Ready! Type 'quit' to stop.\n")

# 3. Create a chat loop
while True:
    user_input = input("You: ")
    
    # Check if the user wants to stop
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
        
    # Add user message to the conversation
    messages.append({"role": "user", "content": user_input})
    
    try:
        # 4. Send the whole conversation to the Llama model
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages
        )
        
        # 5. Get the AI reply
        bot_reply = response.choices[0].message.content
        print(f"\nAI: {bot_reply}\n")
        
        # 6. Add AI reply to the history so it remembers past questions
        messages.append({"role": "assistant", "content": bot_reply})
        
    except Exception as e:
        print(f"Error: {e}")