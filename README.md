# 💬 Gemini AI Chatbot

This project implements a sophisticated, conversational AI chatbot using Google's Gemini Pro model. The project features a beautiful, modern, and theme-aware web application built with Streamlit, providing real-time streaming responses for an interactive user experience.

## 🚀 Live Demo

**Web Application**: [Gemini Ai Chatbot](https://gemini-aibot.streamlit.app)

## Project Structure

```
Gemini-AI-Chatbot/
│
├── README.md                 # Project documentation
├── app.py                    # The main Streamlit web application
├── gemini_api.py             # Helper module for Gemini API calls
├── requirements.txt          # Python dependencies for deployment
├── .env                      # Environment variables (for local development)
└── .gitignore                # Specifies files for Git to ignore
```

## AI Model

The project uses the **Google Gemini 1.5 Flash Model** via the official Google Generative AI API. This is a powerful, multimodal large language model capable of handling a wide range of conversational tasks, including:
-   Answering complex questions
-   Generating creative text
-   Summarizing content
-   Writing and debugging code

The API key is sourced from **Google AI Studio**.

## Workflow

1.  **API Key Configuration**
    -   Securely load the Gemini API key from an `.env` file for local development using `python-dotenv`.
    -   For deployment, the key is read from Streamlit's Secrets management.

2.  **Streamlit UI Setup**
    -   Configure the page with a title, icon, and layout.
    -   Inject custom CSS to create a modern, theme-aware interface that adapts to both light and dark modes.

3.  **Session State Management**
    -   Initialize and maintain the conversation history using `st.session_state`.
    -   This ensures the chatbot remembers the context of the current conversation.

4.  **User Input Handling**
    -   Capture user queries through an interactive `st.chat_input` box.
    -   Display the user's message immediately in the chat interface.

5.  **Streaming API Call**
    -   Send the user's prompt to the Gemini API using the `stream=True` parameter.
    -   This initiates a real-time data stream instead of waiting for the full response.

6.  **Displaying Response**
    -   Use `st.write_stream` to render the AI's response token-by-token as it arrives.
    -   This creates a dynamic "typing" effect, significantly improving user experience.

## Key Features

### 🤖 Backend System
-   **Google Gemini API**: Leverages the `gemini-1.5-flash or gemini-2.5-flash` model for fast and intelligent responses.
-   **Streaming Support**: Implements real-time response generation for a dynamic feel.
-   **Secure API Handling**: Uses `python-dotenv` for local development and is compatible with Streamlit Secrets for secure deployment.
-   **Conversation History**: Maintains context throughout a user's session.

### 💻 Web Application
-   🎨 **Beautiful Modern UI**: Custom CSS provides a clean, professional, and visually appealing interface.
-   🌗 **Theme-Aware**: Automatically adapts all UI components (backgrounds, text, icons) to Streamlit's light and dark themes.
-   ⚡ **Real-time Streaming**: Displays AI responses as they are generated, creating an engaging "live typing" effect.
-   📱 **Responsive Layout**: The interface is designed to work seamlessly on both desktop and mobile devices.
-   ✨ **Interactive Sidebar**: Contains developer information, social media links, and a "New Chat" button to reset the conversation.
-   💡 **User-Friendly**: Includes loading spinners and helpful info messages to guide the user.

## Installation & Usage

### Prerequisites
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 💻 Run Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/daivagnaa/Gemini-AI-Chatbot.git
    cd Gemini-AI-Chatbot
    ```
2.  **Create a `.env` file** in the root directory and add your API key:
    ```
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```
3.  **Launch the Web Application:**
    ```bash
    streamlit run app.py
    ```

## ✨ Web Application Features

### 🎨 User Experience
-   **Modern Design**: Clean layout with custom fonts and colors.
-   **Interactive Elements**: Hover effects on social links and a functional "New Chat" button.
-   **Loading Animations**: A "Thinking..." spinner provides feedback while the AI processes a request.
-   **Real-time Feedback**: Streaming responses make the chatbot feel alive and responsive.

### 👨‍💻 Developer Features
-   **Professional Branding**: A dedicated sidebar with developer name and social media links.
-   **Contact Integration**: Direct links to GitHub, LinkedIn, Gmail, and Instagram.
-   **Automatic Dark Theme**: All custom components, including icons, are designed to switch colors automatically with the theme.
-   **Modular Code**: The API logic is separated into `gemini_api.py` for clean and maintainable code.

## 🛠 Technologies Used

-   **Python 3.x**: Core programming language.
-   **Streamlit**: For building and deploying the interactive web application.
-   **Google Generative AI SDK**: The official Python client for the Gemini API.
-   **Python-Dotenv**: To manage environment variables for local development.
-   **HTML/CSS**: For custom styling and UI enhancements.

## 🌐 Deployment

The application is designed for easy deployment on **Streamlit Community Cloud**.

1.  **Push your code to a public GitHub repository.** (Ensure your `.env` file is in `.gitignore` and not pushed).
2.  **Go to [share.streamlit.io](https://share.streamlit.io/)** and link your GitHub repository.
3.  **Add your API Key to Secrets**: In your app's settings, go to **Settings > Secrets** and add your API key in the following format:
    ```
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```
4.  **Deploy!** Streamlit will handle the rest.

## 🔮 Future Enhancements

-   [ ] 🖼️ Add multimodal support for image-based queries.
-   [ ] 💾 Implement a database (like SQLite or Firebase) to store and retrieve chat history.
-   [ ] 🗣️ Add text-to-speech and speech-to-text functionality.
-   [ ] ⚙️ Allow users to select different Gemini models or adjust parameters (e.g., temperature).
-   [ ] 🔐 Implement user authentication to manage separate chat histories.

## 👨‍💻 Developer

**Daivagna Parmar**
-   📧 **Email**: [devparmar1895@gmail.com](mailto:devparmar1895@gmail.com)
-   🔗 **GitHub**: [@daivagnaa](https://github.com/daivagnaa)
-   💼 **LinkedIn**: [Daivagna Parmar](https://in.linkedin.com/in/daivagna-parmar-949315316)

## 📜 License & Disclaimer

This project is licensed under the MIT License. The responses generated by the AI are for informational purposes and should be used responsibly.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for suggestions and improvements.

---

*This project demonstrates how to build a feature-rich, production-ready AI application using the Gemini API and Streamlit, focusing on a high-quality user experience.*

**⭐ Star this repository if you found it helpful!**