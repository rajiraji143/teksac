import streamlit as st
from datetime import datetime
import random
from PIL import Image
import base64
from io import BytesIO
import os

# Page configuration
st.set_page_config(
    page_title="Tek SAC",
    layout="centered",
    initial_sidebar_state="collapsed"  # Changed to collapsed
)

# Function to convert image to base64
def img_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Define possible full file paths for the background image and logo
image_paths = ["images/vwlogo2.png"]
    
    
    
    


logo_paths = ["images/TEK_Knockout_Logo.png"]
    


# Load and convert the background image to base64
background_base64 = None
for path in image_paths:
    try:
        background_img = Image.open(path)
        background_base64 = img_to_base64(background_img)
        break
    except FileNotFoundError:
        continue
    except Exception as e:
        st.error(f"Error loading image from {path}: {str(e)}")
        continue

# Load and convert the logo to base64
logo_base64 = None
for path in logo_paths:
    try:
        logo_img = Image.open(path)
        # Resize logo to appropriate dimensions
        logo_img = logo_img.resize((150, 50))
        logo_base64 = img_to_base64(logo_img)
        break
    except FileNotFoundError:
        continue
    except Exception as e:
        st.error(f"Error loading logo from {path}: {str(e)}")
        continue

if not background_base64:
    st.error("Background image not found at any specified path. Please check the following locations:")
    for path in image_paths:
        try:
            files = os.listdir(os.path.dirname(path))
            st.write(f"Files in {os.path.dirname(path)}: {files}")
        except Exception:
            st.write(f"Could not access {os.path.dirname(path)}")

if not logo_base64:
    st.error("Logo not found at any specified path. Please check the following locations:")
    for path in logo_paths:
        try:
            files = os.listdir(os.path.dirname(path))
            st.write(f"Files in {os.path.dirname(path)}: {files}")
        except Exception:
            st.write(f"Could not access {os.path.dirname(path)}")

# CSS for dark theme with background image, logo, and sidebar
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .stApp {{
        background-color: #1C2333;
        color: #F5F9FC;
        font-family: 'Inter', sans-serif;
        background-image: url('data:image/png;base64,{background_base64 if background_base64 else ""}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    .main {{
        background-color: transparent;
    }}
    .stMarkdown {{
        color: #F5F9FC;
        font-family: 'Inter', sans-serif;
    }}
    h1 {{
        font-family: 'Inter', sans-serif !important;
        font-weight: 300 !important;
        letter-spacing: -0.03em !important;
    }}
    /* Logo styling */
    .logo-container {{
        position: absolute;
        top: 10px;
        left: 10px;
        z-index: 1000;
    }}
    .logo-img {{
        height: 50px;
        width: auto;
    }}
    /* Chat input styling */
    .stChatInput > div > div {{
        background-color: rgba(28, 35, 51, 0.8) !important;
        border: 1px solid #4A5568 !important;
    }}
    .stChatInput > div > div > textarea {{
        background-color: rgba(28, 35, 51, 0.8) !important;
        color: #F5F9FC !important;
        border: none !important;
        font-family: 'Inter', sans-serif !important;
    }}
    .stChatInput > div > div > textarea::placeholder {{
        color: #A0AEC0 !important;
    }}
    /* Send button styling */
    .stChatInput button {{
        background-color: #2D3748 !important;
        color: #F5F9FC !important;
        border: 1px solid #4A5568 !important;
    }}
    .stChatInput button:hover {{
        background-color: #4A5568 !important;
        border-color: #68D391 !important;
    }}
    /* Chat messages styling */
    .stChatMessage {{
        font-family: 'Inter', sans-serif !important;
        background-color: rgba(28, 35, 51, 0.9) !important;
        padding: 10px;
        border-radius: 5px;
    }}
    /* Sidebar styling */
    [data-testid="stSidebar"] {{
        background-color: #1C2333;
        color: #F5F9FC;
        font-family: 'Inter', sans-serif;
        border-right: 1px solid #4A5568;
    }}
    [data-testid="stSidebar"] .stButton > button {{
        background-color: #2D3748;
        color: #F5F9FC;
        border: 1px solid #4A5568;
        border-radius: 5px;
        padding: 8px 16px;
        margin: 5px 0;
        width: 100%;
        text-align: left;
    }}
    [data-testid="stSidebar"] .stButton > button:hover {{
        background-color: #4A5568;
        border-color: #68D391;
    }}
    [data-testid="stSidebar"] .sidebar-section {{
        padding: 10px;
        border-bottom: 1px solid #4A5568;
    }}
    [data-testid="stSidebar"] .user-profile {{
        text-align: center;
        padding: 20px;
    }}
    [data-testid="stSidebar"] .user-profile img {{
        border-radius: 50%;
        width: 80px;
        height: 80px;
        margin-bottom: 10px;
    }}
    [data-testid="stSidebar"] .user-profile p {{
        color: #A0AEC0;
        font-size: 14px;
        margin: 5px 0;
    }}
</style>
""", unsafe_allow_html=True)

# Add logo to top left corner
if logo_base64:
    st.markdown(
        f'<div class="logo-container"><img src="data:image/png;base64,{logo_base64}" class="logo-img"></div>',
        unsafe_allow_html=True
    )

# Sidebar content
with st.sidebar:
    # User profile section
    
    
    # Navigation section
    st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
    if st.button("Home"):
        st.session_state.messages = []  # Clear chat history on Home
    if st.button("New Chat"):
        st.session_state.messages = []  # Clear chat history for new chat
    if st.button("Settings"):
        st.write("Settings page would go here")
    if st.button("Help"):
        st.write("Help page would go here")
    st.markdown('</div>', unsafe_allow_html=True)

# Header (moved down to account for logo)
st.markdown("<br><br><br>", unsafe_allow_html=True)  # Add space for the logo

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
if prompt := st.chat_input("Ask me anything..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)
    
    # Generate and display assistant response
    response = get_ai_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    with st.chat_message("assistant"):
        st.write(response)