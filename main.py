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
model = genai.GenerativeModel('gemini-1.5-flash')

app = FastAPI()

# Allow your local HTML file to communicate with this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

class StudyMaterial(BaseModel):
    content: str

@app.post("/simplify")
async def simplify_notes(data: StudyMaterial):
    # The prompt that gives the AI its "Study Buddy" persona
    prompt = (
        "You are a helpful Study Buddy. Simplify the following text into "
        "concise, easy-to-read bullet points for a final exam review. "
        f"Text: {data.content}"
    )
    
    response = model.generate_content(prompt)
    return {"simplified_notes": response.text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)