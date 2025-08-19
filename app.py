import streamlit as st
import gemini_api  # Assumes gemini_api.py is updated for streaming

# ---- Page Configuration ----
st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ---- Custom CSS for a modern, responsive, and theme-aware UI ----
st.markdown("""
    <style>
        /* Define theme variables for light and dark mode */
        :root {
            --bg-color-light: #f0f2f6;
            --bg-color-dark: #1a1a1a;
            --sidebar-bg-light: #ffffff;
            --sidebar-bg-dark: #262730;
            --text-color-light: #2d3a4b;
            --text-color-dark: #fafafa;
            --primary-color: #007bff;
        }

        /* Apply variables based on Streamlit's theme */
        body[data-theme="light"] {
            --bg-color: var(--bg-color-light);
            --sidebar-bg: var(--sidebar-bg-light);
            --text-color: var(--text-color-light);
            --icon-filter: invert(0);
        }
        body[data-theme="dark"] {
            --bg-color: var(--bg-color-dark);
            --sidebar-bg: var(--sidebar-bg-dark);
            --text-color: var(--text-color-dark);
            --icon-filter: invert(1);
        }

        /* General Body and App Styling */
        .stApp {
            background-color: var(--bg-color);
        }

        /* Main Title and Subtitle */
        .main-title {
            font-size: 2.8rem; font-weight: 700; color: var(--text-color);
            text-align: center; margin-bottom: 0.2em;
        }
        .subtitle {
            font-size: 1.2rem; color: var(--text-color);
            text-align: center; margin-bottom: 2em; opacity: 0.8;
        }

        /* Chat Message Styling */
        .stChatMessage {
            border-radius: 16px !important; padding: 1.1em 1.5em !important;
            margin-bottom: 1em !important; box-shadow: 0 2px 12px rgba(0,0,0,0.05);
            border: 1px solid transparent;
        }
        [data-testid="chat-message-container-user"] {
            background-color: var(--primary-color, #007bff);
            color: white;
        }
        [data-testid="chat-message-container-assistant"] {
            background-color: var(--secondary-background-color, #ffffff);
        }

        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: var(--sidebar-bg);
            border-right: 1px solid rgba(128, 128, 128, 0.2);
        }
        .sidebar-title {
            font-size: 1.5rem; font-weight: 600; color: var(--text-color);
            margin-bottom: 0.5em; text-align: center;
        }
        .sidebar-subtitle {
            font-size: 1rem; color: var(--text-color); opacity: 0.7;
            text-align: center; margin-bottom: 1.5em;
        }
        .sidebar-social {
            display: flex; flex-direction: column; align-items: center;
            margin-top: 2em; gap: 1em;
        }
        .sidebar-social a {
            text-decoration: none; color: var(--text-color);
            font-size: 1.1rem; display: flex; align-items: center; gap: 0.7em;
            transition: color 0.2s ease-in-out;
        }
        .sidebar-social a:hover {
            color: var(--primary-color);
        }
        .sidebar-social img {
            width: 24px; height: 24px;
            filter: var(--icon-filter);
        }
    </style>
""", unsafe_allow_html=True)


# ---- Sidebar Content ----
with st.sidebar:
    st.markdown('<div class="sidebar-title">Developed by<br>Daivagna Parmar</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-subtitle">AI Chatbot powered by Gemini</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="sidebar-social">
            <a href="https://github.com/daivagnaa" target="_blank"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/github/github-original.svg" alt="GitHub"/> GitHub</a>
            <a href="https://in.linkedin.com/in/daivagna-parmar-949315316" target="_blank"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linkedin/linkedin-plain.svg" alt="LinkedIn"/> LinkedIn</a>
            <a href="mailto:devparmar1895@gmail.com" target="_blank"><img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/gmail.svg" alt="Gmail"/> Gmail</a>
            <a href="https://www.instagram.com/daivagnaa/" target="_blank"><img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/instagram.svg" alt="Instagram"/> Instagram</a>
        </div>
        """,
        unsafe_allow_html=True
    )


# ---- Main Application ----
st.markdown('<div class="main-title">💬 Gemini AI Chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask me anything! I can help with code, answer questions, and more.</div>', unsafe_allow_html=True)

st.divider()

st.info("This app uses the Gemini API. Your conversations are not stored permanently.")

# Initialize chat session in state
if "chat" not in st.session_state:
    st.session_state.chat = gemini_api.start_new_chat()

# Display chat history
for message in st.session_state.chat.history:
    role = "user" if message.role == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# Handle user input
if prompt := st.chat_input("Type your message here..."):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get and display assistant's response (with streaming)
    with st.chat_message("assistant"):
        try:
            with st.spinner("🧠 Thinking..."):
                # **CORRECTED**: Use the streaming function and st.write_stream
                response_stream = gemini_api.send_message(st.session_state.chat, prompt)
                full_response = st.write(response_stream)
        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.warning("Please check your API key or try again later.")