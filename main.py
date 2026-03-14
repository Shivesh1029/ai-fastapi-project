from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Prompt(BaseModel):
    topic: str

@app.get("/")
def home():
    return {"message": "AI Content Generator API is running"}

@app.post("/generate")
def generate(prompt: Prompt):
    topic = prompt.topic
    return {
        "generated_text": f"This is an AI generated marketing message about {topic}. Welcome to luxury experiences and amazing hospitality."
    }