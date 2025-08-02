from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse, StreamingResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
from pydantic import BaseModel
import ollama


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend domain in production
    allow_methods=["*"],
    allow_headers=["*"],
)


templates = Jinja2Templates(directory="templates")

# Define input model for POST body
class ChatInput(BaseModel):
    text: str

# Serve the HTML frontend
@app.get("/", response_class=HTMLResponse)
async def get_chat_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# API endpoint for chat
@app.post("/chat")
async def chat_api(input: ChatInput):
    user_text = input.text
    # Replace this with your actual logic

    response = ollama.chat(model='llama3.2:1b', messages=[
      {
        'role': 'system',
        'content': 'Respond clearly and concisely. Do not exceed 200 words.',
       },
      {
        'role': 'user',
        'content': input.text,
      },
    ])
    user_text = response['message']['content']

    return {"response": f"{user_text}"}














