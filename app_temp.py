import streamlit as st
import gemini_api  # Import our Gemini functions

# Set up the Streamlit page
st.title("Streamlit Gemini Chatbot")
st.caption("A simple chatbot using the Gemini API")

# Initialize chat session in Streamlit's session state
# This is crucial for maintaining conversation history
if "chat" not in st.session_state:
    st.session_state.chat = gemini_api.start_new_chat()

# Display the chat history
# st.session_state.chat.history contains the full conversation
for message in st.session_state.chat.history:
    role = "user" if message.role == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# Handle user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get the response from Gemini and display it
    with st.chat_message("assistant"):
        response = st.write(gemini_api.send_message(st.session_state.chat, prompt))