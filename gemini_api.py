import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Configure the API key
try:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found.")
    genai.configure(api_key=api_key)
except Exception as e:
    print(f"Error configuring Gemini API: {e}")

def start_new_chat():
    """Starts a new chat session with a capable Gemini model."""
    # Using a more recent and capable model
    model = genai.GenerativeModel('gemini-2.5-flash') 
    return model.start_chat(history=[])

def send_message(chat, message):
    """Sends a message and waits for the full response. (Non-streaming)"""
    response = chat.send_message(message)
    return response.text

def send_message_stream(chat, message):
    """Sends a message and streams the response back in chunks."""
    try:
        # Use stream=True to get a streaming response
        response = chat.send_message(message, stream=True)
        for chunk in response:
            # Yield each piece of the response as it arrives
            yield chunk.text
    except Exception as e:
        yield f"An error occurred: {e}"