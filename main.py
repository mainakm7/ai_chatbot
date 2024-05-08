import openai
import json
from fastapi import FastAPI, Form, Request
from starlette import status
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

#------------------------------------------------------
#------------------------------------------------------

with open("secrets.json","r") as f:
    secret = json.load(f)

api_key = secret.get("OPENAI_PROJECT_KEY")

openai.api_key=api_key

#------------------------------------------------------
#------------------------------------------------------


app = FastAPI()
templates = Jinja2Templates(directory="ai_chatbot/templates")


@app.get("/", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("home.html",{"request": request})


chatlog = []
chatlog.append({"role":"system", "content": "You are a helpful assistant"})

chat_responses = []


@app.post("/", response_class=HTMLResponse)
async def chat(request: Request, user_input: Annotated[str, Form()]):

    chatlog.append({'role': 'user', 'content': user_input})
    chat_responses.append(user_input)

    response = openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=chatlog,
        temperature=0.8
    )

    bot_response = response.choices[0].message.content
    chatlog.append({'role': 'assistant', 'content': bot_response})
    chat_responses.append(bot_response)

    return templates.TemplateResponse("home.html", {"request": request, "chat_responses": chat_responses})


@app.get("/image", response_class=HTMLResponse)
async def image_page(request: Request):
    return templates.TemplateResponse("image.html", {"request": request}) 


@app.post("/image", response_class=HTMLResponse)
async def image_generate(request: Request, user_input: Annotated[str, Form()]):
    
    response = openai.images.generate(
        promt=user_input,
        n=1,
        size="512x512"
        
    )
    
    image_url = response.data[0].url
    
    return templates.TemplateResponse("image.html", {"request": request, "image_url": image_url})