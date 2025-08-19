import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_api_key():
    """Get API key from environment variables"""
    # Try GEMINI_API_KEY first
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        return api_key
    return None

# Configure the API key
api_key = get_api_key()
if not api_key:
    raise ValueError("❌ API key not found. Please check your .env file.")

genai.configure(api_key=api_key)
print("✅ Gemini API configured successfully")

def start_new_chat():
    """Starts a new chat session with a capable Gemini model."""
    model = genai.GenerativeModel('gemini-1.5-flash') 
    return model.start_chat(history=[])

def send_message(chat, message):
    """Sends a message and waits for the full response. (Non-streaming)"""
    response = chat.send_message(message)
    return response.text

def send_message_stream(chat, message):
    """Sends a message and streams the response back in chunks."""
    try:
        response = chat.send_message(message, stream=True)
        for chunk in response:
            if chunk.text:
                yield chunk.text
    except Exception as e:
        yield f"An error occurred: {e}"