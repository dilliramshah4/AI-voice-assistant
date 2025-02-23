import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

async def process_input(text: str) -> dict:
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = await model.generate_content_async(text)
        return {
            "message": response.text,
            "intent": "general"
        }
    except Exception as e:
        return {"message": str(e), "intent": "error"}