import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def start_new_chat():
    model = genai.GenerativeModel('gemini-2.5-flash')
    return model.start_chat(history=[])

def send_message(chat, message):
    response = chat.send_message(message)
    return response.text