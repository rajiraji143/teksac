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
    initial_sidebar_state="collapsed"
)

# Function to convert image to base64
def img_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Define possible full file paths for the background image
image_paths = [
    r"C:\Users\TekAn\Documents\vwlogo2.png",
    r"C:\Users\TekAn\Documents\tek_logo_no_vw.png",
    r"C:\Users\TekAn\Documents\tek_logo_no_vw.png.png",
    r"C:\Users\TekAn\Desktop\Azure folder\tek_logo_no_vw.png"
]

# Define file path for the logo (used for both sidebar and main logo)
logo_path = r"C:\Users\TekAn\Documents\Tek Logo.png"

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
logo_icon_base64 = None  # For assistant avatar
try:
    logo_img = Image.open(logo_path)
    # Resize logo to appropriate dimensions for main logo (50px height)
    logo_img_main = logo_img.resize((150, 50))
    logo_base64 = img_to_base64(logo_img_main)
    # Create a smaller version for the assistant icon (32x32)
    logo_img_icon = logo_img.resize((32, 32))
    logo_icon_base64 = img_to_base64(logo_img_icon)
except FileNotFoundError:
    st.error(f"Logo not found at {logo_path}. Please check the file path.")
except Exception as e:
    st.error(f"Error loading logo from {logo_path}: {str(e)}")

if not background_base64:
    st.error("Background image not found at any specified path. Please check the following locations:")
    for path in image_paths:
        try:
            files = os.listdir(os.path.dirname(path))
            st.write(f"Files in {os.path.dirname(path)}: {files}")
        except Exception:
            st.write(f"Could not access {os.path.dirname(path)}")

if not logo_base64:
    st.error(f"Logo not found at {logo_path}. Please check the file path.")

# CSS for dark theme with background image and sidebar
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
    h1, h2, h3, h4, h5, h6 {{
        font-family: 'Inter', sans-serif !important;
        font-weight: 300 !important;
        letter-spacing: -0.03em !important;
        color: #8A9EB0 !important;
    }}
    /* Planning Assistant specific styling */
    .planning-assistant {{
        color: #6E7F8F !important;
        font-weight: 400 !important;
        margin-bottom: 1.5rem !important;
        text-shadow: 0.5px 0.5px 1px rgba(0,0,0,0.1);
    }}
    /* Main logo styling */
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
    /* Sidebar logo styling */
    .sidebar-logo {{
        text-align: center;
        padding: 20px;
    }}
    .sidebar-logo img {{
        width: 120px;
        height: auto;
        margin-bottom: 10px;
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
    /* Chat messages styling - white background */
    .message-container {{
        background-color: #FFFFFF !important;
        color: #1C2333 !important;
        padding: 12px;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin: 8px 0;
    }}
    /* Custom avatar styling */
    .custom-avatar {{
        width: 32px !important;
        height: 32px !important;
        border-radius: 50% !important;
        object-fit: cover !important;
        margin-top: 12px !important;
    }}
    /* Sidebar styling */
    [data-testid="stSidebar"] {{
        background-color: #FFFFFF;
        color: #1C2333;
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
</style>
""", unsafe_allow_html=True)

# Add main logo to top left corner
if logo_base64:
    st.markdown(
        f'<div class="logo-container"><img src="data:image/png;base64,{logo_base64}" class="logo-img"></div>',
        unsafe_allow_html=True
    )

# Sidebar content
with st.sidebar:
    # Sidebar logo
    if logo_base64:
        st.markdown(
            f'<div class="sidebar-logo"><img src="data:image/png;base64,{logo_base64}" alt="Sidebar Logo"></div>',
            unsafe_allow_html=True
        )
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

# Updated "Your Planning Assistant" heading
st.markdown("""
<h3 class="planning-assistant">Your Planning Assistant</h3>
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    if message["role"] == "assistant":
        # Custom layout for assistant messages with TEK logo
        col1, col2 = st.columns([0.1, 0.9])
        with col1:
            if logo_icon_base64:
                st.markdown(
                    f'<img src="data:image/png;base64,{logo_icon_base64}" class="custom-avatar">',
                    unsafe_allow_html=True
                )
        with col2:
            st.markdown(f'<div class="message-container">{message["content"]}</div>', unsafe_allow_html=True)
    else:
        # Standard layout for user messages
        with st.chat_message("user"):
            st.markdown(f'<div class="message-container">{message["content"]}</div>', unsafe_allow_html=True)

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
        return "For web development, I recommend using a modern framework like React or Vue.js with a robust backend API. Consider implementing responsive design principles and optimizing for performance from the start."
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
        st.markdown(f'<div class="message-container">{prompt}</div>', unsafe_allow_html=True)
    
    # Generate and display assistant response
    response = get_ai_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Custom layout for assistant response with TEK logo
    col1, col2 = st.columns([0.1, 0.9])
    with col1:
        if logo_icon_base64:
            st.markdown(
                f'<img src="data:image/png;base64,{logo_icon_base64}" class="custom-avatar">',
                unsafe_allow_html=True
            )
    with col2:
        st.markdown(f'<div class="message-container">{response}</div>', unsafe_allow_html=True)