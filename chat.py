from dotenv import load_dotenv
from openai import OpenAI
import requests
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat():
    while(True):
        a = input("You: ")
        if a == "exit":
            exit()
        else:
            b = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": a}],
                max_tokens=1024,
                temperature=0.5, # controls the randomness of the output
            )
            print("Bot: " + b.choices[0].message.content)
   

if __name__ == "__main__":
    chat()
