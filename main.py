import openai
import json

with open("secrets.json","r") as f:
    secret = json.load(f)

api_key = secret.get("OPENAI_PROJECT_KEY")

openai.api_key=api_key

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role":"system",
        "content":"You are a helpful assistant"
    },{
        "role":"user",
        "content":"What is Python?"
    }]
)

print(response)