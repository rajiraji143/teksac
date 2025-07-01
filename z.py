import streamlit as st
from datetime import datetime
import random

# Page configuration
st.set_page_config(
    page_title="Tek SAC",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS for dark theme with new background color
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
   
    .stApp {
        background-color: #1A3C34; /* Updated to dark teal */
        color: #F5F9FC;
        font-family: 'Inter', sans-serif;
        min-height: 100vh;
    }
    .main {
        background-color: transparent;
    }
    .stMarkdown {
        color: #F5F9FC;
        font-family: 'Inter', sans-serif;
    }
    h1, h3 {
        font-family: 'Inter', sans-serif !important;
        font-weight: 300 !important;
        letter-spacing: -0.03em !important;
        margin-top: 0.5rem !important;
    }
    .main .block-container {
        padding-top: 20px !important; /* Reduced since no logo */
    }
    .stChatInput > div > div {
        background-color: rgba(28, 35, 51, 0.8) !important;
        border: 1px solid #4A5568 !important;
    }
    .stChatInput > div > div > textarea {
        background-color: rgba(28, 35, 51, 0.8) !important;
        color: #F5F9FC !important;
        border: none !important;
        font-family: 'Inter', sans-serif !important;
    }
    .stChatInput > div > div > textarea::placeholder {
        color: #A0AEC0 !important;
    }
    .stChatInput button {
        background-color: #2D3748 !important;
        color: #F5F9FC !important;
        border: 1px solid #4A5568 !important;
    }
    .stChatInput button:hover {
        background-color: #4A5568 !important;
        border-color: #68D391 !important;
    }
    .stChatMessage {
        font-family: 'Inter', sans-serif !important;
        background-color: rgba(28, 35, 51, 0.9) !important;
        padding: 10px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Header content
st.markdown("# Tek SAC")
st.markdown("### Your Planning Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# AI response function
def get_ai_response(user_message):
    responses = [
        "I understand your request. Let me provide you with a comprehensive solution that addresses your specific needs while maintaining best practices.",
        "That's an excellent question! Based on your requirements, I recommend implementing a scalable architecture that prioritizes both performance and maintainability.",
        "I can help you with that. Here's a detailed approach that takes into account modern development practices and industry standards.",
        "Great idea! Let me break this down into actionable steps that will help you achieve your goals efficiently and effectively."
    ]
   
    lower_message = user_message.lower()
    if any(word in lower_message for word in ['web', 'app', 'website']):
        return "For web development, I recommend using modern frameworks like React or Vue.js with a robust backend API. Consider implementing responsive design principles and optimizing for performance from the start."
    elif any(word in lower_message for word in ['database', 'data']):
        return "For data management, consider using PostgreSQL for relational data or MongoDB for document storage. Implement proper indexing strategies and consider data caching layers like Redis for improved performance."
    elif any(word in lower_message for word in ['machine learning', 'ai', 'ml']):
        return "For machine learning projects, I suggest starting with Python and libraries like scikit-learn or TensorFlow. Focus on data preprocessing, feature engineering, and model validation techniques."
    else:
        return random.choice(responses)

# Chat input
if prompt := st.chat_input("Ask Tek SAC anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    response = get_ai_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)