from dotenv import load_dotenv
import openai
import requests

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY") 

def chat():
    while(True):
        a = input("You: ")
        if a == "exit":
            exit()
        else:
            b = openai.Completion.create(
                engine="text-davinci-002",
                prompt=a,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5, # controls the randomness of the output
            )
            print("Bot: " + b.choices[0].text)
   

if __name__ == "__main__":
    chat()
