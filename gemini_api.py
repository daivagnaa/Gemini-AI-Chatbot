import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st

# Load variables from .env file
load_dotenv()

# Configure the API key
try:
    # Change this line to match your .env variable name
    api_key = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment or secrets.")
    genai.configure(api_key=api_key)
except Exception as e:
    print(f"Error configuring Gemini API: {e}")

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
            yield chunk.text
    except Exception as e:
        yield f"An error occurred: {e}"