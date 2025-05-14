from config import OPENAI_API_KEY
import openai

openai.api_key = OPENAI_API_KEY

def ask_agent(chat_input, search_results):
    context = search_results[0]['metadata']['text'] if search_results else ""
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that connects user input with matching memories or stories."},
            {"role": "user", "content": f"User said: {chat_input}\nRelated story: {context}"}
        ]
    )
    
    return response['choices'][0]['message']['content']
