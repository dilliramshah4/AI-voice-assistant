from fastapi import FastAPI
from pydantic import BaseModel
from app.nlp_processing import process_input
from app.logging_config import logger

app = FastAPI()

class TextInput(BaseModel):
    text: str

# Verify endpoint path matches your request
@app.post("/process-text/")  # Must match your curl command
async def process_text(input: TextInput):
    try:
        response = await process_input(input.text)
        logger.info(f"Processed: {input.text}")
        return {"response": response}
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {"error": str(e)}

@app.get("/process-voice/")
def process_voice_get():
    return {"message": "Use POST to send data to this endpoint."}
