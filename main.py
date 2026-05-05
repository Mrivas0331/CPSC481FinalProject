import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))

# Use the fast, efficient model
model = genai.GenerativeModel('gemini-2.5-flash')

app = FastAPI()

# Allow your local HTML file to communicate with this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: list[ChatMessage]

@app.post("/chat")
async def chat(data: ChatRequest):
    conversation = ""
    for msg in data.messages:
        conversation += f"{msg.role}: {msg.content}\n"

    # The prompt that gives the AI its "Study Buddy" persona
    prompt = (
        "You are Study Steve, a friendly AI study buddy. Your goal "
        "is to help the user study and understand the material,"
        "not just provide answers.\n\n"
        "Step 1: simplify the content into short bullet points (max 5 bullets)."
        "Each bullet must be clear, simple, and under 15 words.\n\n"
        "Step 2: Ask 1-2 questions to test the user's understanding.\n\n"
        "Important Rules:\n"
        "- Keep responses short and easy to read.\n"
        "- Do not explain everything at once.\n"
        "- Do not give full answers immediately.\n"
        "- If user answers correctly, brief confirm and move on.\n"
        "- If user answers incorrectly, provide a hint or a simpler question.\n"
        "- Encourage user to think critically and engage with the material.\n"
        "- Always maintain a supportive and encouraging tone.\n\n"
        "Only output the bullet points and questions.\n\n"
        f"Conversation history: \n{conversation}\n"
        "Study Steve:"
    )
    
    try:
        response = model.generate_content(prompt)
        return {"response": response.text}

    except Exception as e:
        print("Gemini API Error:", e)
        return {
            "response": "Study Steven is currently overloaded 😭 Please wait a moment and try again."
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)