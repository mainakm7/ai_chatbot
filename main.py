import openai
import json

with open("secrets.json","r") as f:
    secret = json.load(f)

api_key = secret.get("OPENAI_PROJECT_KEY")

openai.api_key=api_key

chatlog = []
chatlog.append({"role":"system", "content": "You are a helpful assistant"})
while True:
    uinput = input()
    if uinput.lower() == "stop":
        break
    
    chatlog.append({"role":"user", "content": uinput})

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chatlog,
        temperature=0.8
    )

    assistant_response = response.choices[0].message.content
    chatlog.append({"role": "assistant", "content": assistant_response})
    print(response.choices[0].message.content)

