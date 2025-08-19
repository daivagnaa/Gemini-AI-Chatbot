import streamlit as st
import gemini_api

# ---- Page Configuration ----
st.set_page_config(
    page_title="Gemini AI Chatbot - By Daivagna Parmar",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ---- Custom CSS (Following Diabetes App Pattern) ----
st.markdown("""
    <style>
        .main-header {
            text-align: center;
            color: #2E86AB;
            font-size: 3.5rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        .sub-header {
            text-align: center;
            color: #666;
            font-size: 1.3rem;
            margin-bottom: 2rem;
            font-style: italic;
        }
        .developer-info {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1.5rem;
            border-radius: 15px;
            color: white;
            text-align: center;
            margin: 2rem 0;
        }
        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 25px;
            padding: 0.8rem 3rem;
            font-size: 1.2rem;
            font-weight: bold;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        }
        .stButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
        }
        .info-card {
            background: #f8f9fa;
            padding: 1.5rem;
            border-radius: 12px;
            border-left: 4px solid #667eea;
            margin: 1rem 0;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .contact-info {
            background: transparent;
            padding: 1.5rem;
            border-radius: 12px;
            margin: 1rem 0;
            text-align: center;
        }
        .contact-info h4 {
            color: var(--text-color);
            margin-bottom: 1rem;
            font-size: 1.2rem;
        }
        .contact-info hr {
            border-color: rgba(128, 128, 128, 0.3);
            margin: 1rem 0;
        }
        .social-links {
            display: flex;
            flex-direction: column;
            gap: 0.8rem;
            align-items: center;
        }
        .social-link {
            display: flex;
            align-items: center;
            gap: 0.8rem;
            padding: 0.6rem 1rem;
            border-radius: 8px;
            text-decoration: none !important;  /* Remove underline */
            color: var(--text-color) !important;  /* Force normal text color */
            transition: all 0.3s ease;
            background: rgba(102, 126, 234, 0.1);
            border: 1px solid rgba(102, 126, 234, 0.2);
            width: 100%;
            max-width: 200px;
        }
        .social-link:hover {
            background: rgba(102, 126, 234, 0.2);
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
            color: var(--text-color) !important;  /* Keep normal color on hover */
            text-decoration: none !important;  /* No underline on hover */
        }
        .social-icon {
            width: 20px;
            height: 20px;
            flex-shrink: 0;
        }
        
        /* Dark theme compatibility */
        @media (prefers-color-scheme: dark) {
            .info-card {
                background: rgba(102, 126, 234, 0.1);
                border-left: 4px solid #667eea;
                color: var(--text-color);
            }
            .social-icon {
                filter: brightness(0) invert(1);
            }
        }
    </style>
""", unsafe_allow_html=True)

# ---- Sidebar Content ----
with st.sidebar:

    # Contact Information at Bottom of Sidebar
    st.markdown("""
    <div class="contact-info">
        <h4>Developed by Daivagna Parmar</h4>
        <hr>
        <div class="social-links">
            <a href="https://github.com/daivagnaa" target="_blank" class="social-link">
                <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/github/github-original.svg" 
                     alt="GitHub" class="social-icon">
                GitHub
            </a>
            <a href="https://in.linkedin.com/in/daivagna-parmar-949315316" target="_blank" class="social-link">
                <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linkedin/linkedin-plain.svg"
                     alt="LinkedIn" class="social-icon">
                LinkedIn
            </a>
            <a href="https://www.instagram.com/daivagnaa/" target="_blank" class="social-link">
                <img src="https://www.svgrepo.com/show/424911/instagram-logo-facebook-2.svg" 
                     alt="Instagram" class="social-icon">
                Instagram
            </a>
            <a href="mailto:devparmar1895@gmail.com" class="social-link">
                <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/gmail.svg" 
                     alt="Gmail" class="social-icon">
                Gmail
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---- Main Application ----
st.markdown('<h1 class="main-header">💬 Gemini AI Chatbot</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Advanced AI-Powered Conversation Assistant (Gemini Flash 1.5)</p>', unsafe_allow_html=True)

# Initialize chat
if "chat" not in st.session_state:
    st.session_state.chat = gemini_api.start_new_chat()

if not st.session_state.chat.history:
    st.info("This app uses the Gemini API. Your conversations are not stored permanently.")

# Chat history
for message in st.session_state.chat.history:
    role = "user" if message.role == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# User input
if prompt := st.chat_input("Type your message here..."):
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            with st.spinner("🧠 Thinking..."):
                response_stream = gemini_api.send_message_stream(st.session_state.chat, prompt)
                full_response = st.write_stream(response_stream)
        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.warning("Please check your API key or try again later.")
