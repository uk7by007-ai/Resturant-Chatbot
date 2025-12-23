"""
Bella Vista Restaurant - AI Chatbot Application
Premium Streamlit Interface with Voice Capabilities
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import base64
from pathlib import Path
import os

# Import custom modules
from chatbot_engine import RestaurantChatbot
from booking_system import BookingSystem
from voice_handler import VoiceHandler
from restaurant_data import MENU_DATA, SPECIAL_OFFERS, get_popular_items
from config import APP_TITLE, APP_SUBTITLE, RESTAURANT_INFO, BOOKING_SLOTS

# Page configuration
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to get base64 encoded image
def get_base64_image(image_path):
    """Convert image to base64 for embedding in CSS"""
    try:
        if os.path.exists(image_path):
            with open(image_path, "rb") as image_file:
                import base64
                encoded = base64.b64encode(image_file.read()).decode()
                return f"data:image/png;base64,{encoded}"
    except:
        pass
    return ""

# Load custom CSS
def load_css():
    # Get base64 encoded images
    chef_bg = get_base64_image("images/chef_cooking_bg.png")
    pizza_bg = get_base64_image("images/pizza_restaurant_bg.png")
    restaurant_bg = get_base64_image("images/restaurant_interior_bg.png")
    food_bg = get_base64_image("images/gourmet_food_bg.png")
    css = f"""
    <style>
    /* Import Modern Eye-Catching Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');
    
    /* Global Styles with Dark-Pastel Fusion */
    .stApp {{
        background: 
            linear-gradient(135deg, 
                rgba(26, 22, 37, 0.85) 0%, 
                rgba(45, 27, 64, 0.8) 15%, 
                rgba(232, 213, 255, 0.3) 35%, 
                rgba(255, 229, 229, 0.3) 50%, 
                rgba(212, 241, 244, 0.3) 65%, 
                rgba(45, 27, 64, 0.8) 85%, 
                rgba(26, 22, 37, 0.85) 100%),
            url('{restaurant_bg}');
        background-size: 400% 400%, cover;
        background-position: center, center;
        background-attachment: fixed, fixed;
        animation: gradientShift 20s ease infinite;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        font-size: 16px;
        color: #1F2937;
    }}
    
    @keyframes gradientShift {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}
    
    /* Main container */
    .main .block-container {{
        padding: 2.5rem;
        max-width: 1400px;
    }}
    
    /* Header styling - Eye-catching with perfect contrast */
    .restaurant-header {{
        text-align: center;
        padding: 4rem 3rem;
        background: 
            linear-gradient(135deg, 
                rgba(26, 22, 37, 0.92) 0%, 
                rgba(45, 27, 64, 0.92) 50%, 
                rgba(88, 28, 135, 0.88) 100%),
            url('{chef_bg}');
        background-size: cover, cover;
        background-position: center, center;
        backdrop-filter: blur(30px);
        border-radius: 35px;
        border: 3px solid;
        border-image: linear-gradient(135deg, #C4B5FD, #F9A8D4, #FDE68A) 1;
        margin-bottom: 3rem;
        box-shadow: 0 25px 70px rgba(168, 85, 247, 0.4),
                    0 10px 30px rgba(236, 72, 153, 0.3),
                    inset 0 1px 0 rgba(255, 255, 255, 0.1);
        position: relative;
        overflow: hidden;
    }}
    
    .restaurant-header::before {{
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, 
            transparent, 
            rgba(196, 181, 253, 0.3), 
            transparent);
        animation: shimmer 4s infinite;
    }}
    
    @keyframes shimmer {{
        0% {{ transform: translateX(-100%) translateY(-100%) rotate(45deg); }}
        100% {{ transform: translateX(100%) translateY(100%) rotate(45deg); }}
    }}
    
    .restaurant-title {{
        font-family: 'Outfit', sans-serif;
        font-size: 5rem;
        font-weight: 900;
        background: linear-gradient(135deg, 
            #FDE68A 0%, 
            #FCA5A5 25%, 
            #F9A8D4 50%, 
            #C4B5FD 75%, 
            #A5F3FC 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        position: relative;
        z-index: 1;
        letter-spacing: 2px;
        text-transform: uppercase;
        filter: drop-shadow(0 4px 12px rgba(253, 230, 138, 0.5));
        line-height: 1.2;
    }}
    
    .restaurant-subtitle {{
        font-family: 'Space Grotesk', monospace;
        font-size: 1.5rem;
        font-weight: 500;
        color: #FDE68A;
        position: relative;
        z-index: 1;
        letter-spacing: 3px;
        text-transform: uppercase;
        text-shadow: 0 2px 10px rgba(253, 230, 138, 0.5);
    }}
    
    /* Chat container - High contrast for readability */
    .chat-container {{
        background: 
            linear-gradient(135deg, 
                rgba(255, 255, 255, 0.96) 0%, 
                rgba(254, 243, 199, 0.93) 100%),
            url('{pizza_bg}');
        background-size: cover, cover;
        background-position: center, center;
        border-radius: 30px;
        padding: 2.5rem;
        min-height: 500px;
        max-height: 600px;
        overflow-y: auto;
        box-shadow: 0 15px 50px rgba(168, 85, 247, 0.2),
                    0 5px 15px rgba(236, 72, 153, 0.15),
                    inset 0 1px 0 rgba(255, 255, 255, 1);
        margin-bottom: 2rem;
        border: 2px solid rgba(196, 181, 253, 0.5);
    }}
    
    /* Message bubbles - Enhanced readability with dark text on pastel */
    .user-message {{
        background: linear-gradient(135deg, #1F2937 0%, #374151 100%);
        color: #FDE68A;
        padding: 1.5rem 2rem;
        border-radius: 28px 28px 8px 28px;
        margin: 1rem 0;
        margin-left: auto;
        max-width: 78%;
        float: right;
        clear: both;
        box-shadow: 0 6px 20px rgba(31, 41, 55, 0.4),
                    0 2px 8px rgba(0, 0, 0, 0.2);
        animation: slideInRight 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
        font-weight: 500;
        font-size: 1.1rem;
        line-height: 1.7;
        border: 2px solid rgba(253, 230, 138, 0.3);
    }}
    
    .bot-message {{
        background: linear-gradient(135deg, #C4B5FD 0%, #DDD6FE 100%);
        color: #1F2937;
        padding: 1.5rem 2rem;
        border-radius: 28px 28px 28px 8px;
        margin: 1rem 0;
        max-width: 78%;
        float: left;
        clear: both;
        box-shadow: 0 6px 20px rgba(168, 85, 247, 0.3),
                    0 2px 8px rgba(139, 92, 246, 0.2);
        animation: slideInLeft 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
        font-weight: 500;
        font-size: 1.1rem;
        line-height: 1.7;
        border: 2px solid rgba(196, 181, 253, 0.5);
    }}
    
    @keyframes slideInRight {{
        from {{
            opacity: 0;
            transform: translateX(40px) scale(0.9);
        }}
        to {{
            opacity: 1;
            transform: translateX(0) scale(1);
        }}
    }}
    
    @keyframes slideInLeft {{
        from {{
            opacity: 0;
            transform: translateX(-40px) scale(0.9);
        }}
        to {{
            opacity: 1;
            transform: translateX(0) scale(1);
        }}
    }}
    
    /* Buttons - Eye-catching with excellent visibility */
    .stButton > button {{
        background: linear-gradient(135deg, #1F2937 0%, #374151 50%, #4B5563 100%);
        color: #FDE68A;
        border: 2px solid #FDE68A;
        border-radius: 18px;
        padding: 1rem 2.5rem;
        font-family: 'Outfit', sans-serif;
        font-weight: 700;
        font-size: 1.1rem;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        box-shadow: 0 8px 25px rgba(31, 41, 55, 0.4),
                    0 3px 10px rgba(253, 230, 138, 0.3);
        letter-spacing: 1px;
        text-transform: uppercase;
    }}
    
    .stButton > button:hover {{
        transform: translateY(-4px) scale(1.05);
        box-shadow: 0 15px 40px rgba(168, 85, 247, 0.5),
                    0 5px 15px rgba(253, 230, 138, 0.5);
        background: linear-gradient(135deg, #F9A8D4 0%, #C4B5FD 50%, #A5F3FC 100%);
        color: #1F2937;
        border-color: #C4B5FD;
    }}
    
    .stButton > button:active {{
        transform: translateY(-2px) scale(1.02);
    }}
    
    /* Input fields - Clear and visible */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {{
        border-radius: 18px;
        border: 3px solid rgba(196, 181, 253, 0.6);
        transition: all 0.3s ease;
        background: rgba(255, 255, 255, 0.98);
        padding: 1rem 1.3rem;
        font-family: 'Inter', sans-serif;
        font-size: 1.05rem;
        font-weight: 500;
        color: #1F2937;
    }}
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {{
        border-color: #C4B5FD;
        box-shadow: 0 0 0 5px rgba(196, 181, 253, 0.2),
                    0 6px 20px rgba(168, 85, 247, 0.2);
        background: white;
        outline: none;
    }}
    
    /* Sidebar - Dark theme with pastel accents */
    .css-1d391kg, [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, 
            rgba(26, 22, 37, 0.95) 0%, 
            rgba(45, 27, 64, 0.95) 100%);
        backdrop-filter: blur(25px);
        border-right: 3px solid rgba(196, 181, 253, 0.5);
    }}
    
    [data-testid="stSidebar"] * {{
        color: #F3F4F6 !important;
        font-weight: 500;
    }}
    
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {{
        color: #FDE68A !important;
        font-family: 'Outfit', sans-serif;
        font-weight: 700;
        letter-spacing: 1px;
    }}
    
    /* Menu cards - Premium design with high contrast */
    .menu-card {{
        background: 
            linear-gradient(135deg, 
                rgba(255, 255, 255, 0.97) 0%, 
                rgba(254, 243, 199, 0.7) 100%),
            url('{food_bg}');
        background-size: cover, cover;
        background-position: center, center;
        border-radius: 25px;
        padding: 2.5rem;
        margin: 1.5rem 0;
        box-shadow: 0 8px 30px rgba(168, 85, 247, 0.18),
                    0 3px 12px rgba(236, 72, 153, 0.12);
        transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
        border: 3px solid rgba(196, 181, 253, 0.4);
        position: relative;
        overflow: hidden;
    }}
    
    .menu-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, 
            rgba(196, 181, 253, 0.2) 0%, 
            rgba(249, 168, 212, 0.2) 100%);
        opacity: 0;
        transition: opacity 0.5s ease;
    }}
    
    .menu-card:hover::before {{
        opacity: 1;
    }}
    
    .menu-card:hover {{
        transform: translateY(-10px) scale(1.03);
        box-shadow: 0 20px 50px rgba(168, 85, 247, 0.3),
                    0 8px 20px rgba(236, 72, 153, 0.25);
        border-color: rgba(196, 181, 253, 0.8);
    }}
    
    .menu-item-name {{
        font-family: 'Outfit', sans-serif;
        font-size: 1.7rem;
        font-weight: 800;
        background: linear-gradient(135deg, #7C3AED 0%, #EC4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.8rem;
        position: relative;
        z-index: 1;
        letter-spacing: 0.5px;
    }}
    
    .menu-item-price {{
        font-family: 'Space Grotesk', monospace;
        font-size: 1.6rem;
        font-weight: 700;
        color: #DC2626;
        text-shadow: 0 2px 8px rgba(220, 38, 38, 0.3);
        position: relative;
        z-index: 1;
    }}
    
    /* Info boxes - Dark theme variant */
    .info-box {{
        background: linear-gradient(135deg, 
            rgba(31, 41, 55, 0.95) 0%, 
            rgba(55, 65, 81, 0.95) 100%);
        backdrop-filter: blur(25px);
        border-radius: 25px;
        padding: 2.5rem;
        border: 3px solid rgba(196, 181, 253, 0.5);
        color: #F3F4F6;
        margin: 1.5rem 0;
        box-shadow: 0 10px 35px rgba(31, 41, 55, 0.4),
                    0 4px 15px rgba(168, 85, 247, 0.2);
        transition: all 0.4s ease;
    }}
    
    .info-box:hover {{
        transform: translateY(-5px);
        box-shadow: 0 15px 45px rgba(168, 85, 247, 0.3),
                    0 6px 20px rgba(236, 72, 153, 0.2);
        border-color: rgba(253, 230, 138, 0.6);
    }}
    
    .info-box h3, .info-box h4 {{
        font-family: 'Outfit', sans-serif;
        background: linear-gradient(135deg, #FDE68A 0%, #F9A8D4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800;
        font-size: 1.5rem;
        letter-spacing: 1px;
        margin-bottom: 1rem;
    }}
    
    .info-box p {{
        color: #E5E7EB;
        font-size: 1.05rem;
        line-height: 1.7;
        font-weight: 400;
    }}
    
    /* Hide Streamlit branding */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    
    /* Scrollbar styling - Pastel on dark */
    ::-webkit-scrollbar {{
        width: 12px;
    }}
    
    ::-webkit-scrollbar-track {{
        background: rgba(31, 41, 55, 0.3);
        border-radius: 10px;
    }}
    
    ::-webkit-scrollbar-thumb {{
        background: linear-gradient(135deg, #C4B5FD 0%, #F9A8D4 100%);
        border-radius: 10px;
        border: 3px solid rgba(255, 255, 255, 0.2);
    }}
    
    ::-webkit-scrollbar-thumb:hover {{
        background: linear-gradient(135deg, #A78BFA 0%, #EC4899 100%);
    }}
    
    /* Form elements - Enhanced visibility */
    .stRadio > label, .stCheckbox > label {{
        color: #F3F4F6 !important;
        font-weight: 600;
        font-size: 1.05rem;
    }}
    
    .stSelectbox > div > div {{
        border-radius: 15px;
        border: 3px solid rgba(196, 181, 253, 0.6);
        background: rgba(255, 255, 255, 0.98);
        font-size: 1.05rem;
        font-weight: 500;
    }}
    
    .stNumberInput > div > div > input {{
        border-radius: 15px;
        border: 3px solid rgba(196, 181, 253, 0.6);
        background: rgba(255, 255, 255, 0.98);
        font-size: 1.05rem;
        font-weight: 500;
    }}
    
    .stDateInput > div > div > input {{
        border-radius: 15px;
        border: 3px solid rgba(196, 181, 253, 0.6);
        background: rgba(255, 255, 255, 0.98);
        font-size: 1.05rem;
        font-weight: 500;
    }}
    
    /* Markdown text - Better readability */
    .stMarkdown {{
        font-size: 1.05rem;
        line-height: 1.7;
        color: #1F2937;
    }}
    
    /* Headings - Eye-catching */
    h1, h2, h3, h4, h5, h6 {{
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px !important;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Initialize session state
def init_session_state():
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = RestaurantChatbot()
    if 'booking_system' not in st.session_state:
        st.session_state.booking_system = BookingSystem()
    if 'voice_handler' not in st.session_state:
        st.session_state.voice_handler = VoiceHandler()
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'voice_enabled' not in st.session_state:
        st.session_state.voice_enabled = False

# Display chat messages
def display_chat():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f'<div class="user-message">👤 {message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-message">🤖 {message["content"]}</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Main application
def main():
    load_css()
    init_session_state()
    
    # Header
    st.markdown(f"""
        <div class="restaurant-header">
            <div class="restaurant-title">{APP_TITLE}</div>
            <div class="restaurant-subtitle">{APP_SUBTITLE}</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("### 🎯 Navigation")
        page = st.radio("", ["💬 Chat Assistant", "📅 Make Reservation", "🍽️ View Menu", "ℹ️ Restaurant Info"])
        
        st.markdown("---")
        
        # Voice toggle
        st.markdown("### 🎤 Voice Features")
        voice_enabled = st.checkbox("Enable Voice Input", value=st.session_state.voice_enabled)
        st.session_state.voice_enabled = voice_enabled
        
        if voice_enabled:
            st.info("🎙️ Voice input is enabled. Click 'Listen' to speak.")
        
        st.markdown("---")
        
        # Quick actions
        st.markdown("### ⚡ Quick Actions")
        if st.button("🔄 Clear Chat"):
            st.session_state.messages = []
            st.session_state.chatbot.reset_conversation()
            st.rerun()
        
        if st.button("⭐ Popular Dishes"):
            popular = get_popular_items()
            response = "Here are our most popular dishes:\n\n"
            for item in popular[:5]:
                response += f"• {item['name']} (${item['price']}) - {item['description']}\n"
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
    
    # Main content area
    if page == "💬 Chat Assistant":
        show_chat_page()
    elif page == "📅 Make Reservation":
        show_booking_page()
    elif page == "🍽️ View Menu":
        show_menu_page()
    else:
        show_info_page()

def show_chat_page():
    st.markdown("## 💬 Chat with Our AI Assistant")
    st.markdown("Ask me anything about our menu, hours, specials, or dietary options!")
    
    # Display chat history
    display_chat()
    
    # Input area
    col1, col2, col3 = st.columns([6, 1, 1])
    
    with col1:
        user_input = st.text_input("Your message:", key="user_input", placeholder="Type your question here...")
    
    with col2:
        send_button = st.button("📤 Send")
    
    with col3:
        if st.session_state.voice_enabled:
            listen_button = st.button("🎤 Listen")
        else:
            listen_button = False
    
    # Handle voice input
    if listen_button and st.session_state.voice_enabled:
        with st.spinner("🎤 Listening..."):
            result = st.session_state.voice_handler.listen()
            if result["success"]:
                user_input = result["text"]
                st.success(f"You said: {user_input}")
            else:
                st.error(result["error"])
    
    # Handle text/voice input
    if (send_button or listen_button) and user_input:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Get bot response
        with st.spinner("🤔 Thinking..."):
            response = st.session_state.chatbot.get_response(user_input)
        
        # Add bot response
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Generate voice response if enabled
        if st.session_state.voice_enabled:
            voice_result = st.session_state.voice_handler.speak(response)
            if voice_result["success"]:
                audio_file = open(voice_result["audio_path"], 'rb')
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format='audio/mp3')
        
        st.rerun()

def show_booking_page():
    st.markdown("## 📅 Make a Reservation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Your Information")
        name = st.text_input("Full Name *")
        email = st.text_input("Email *")
        phone = st.text_input("Phone Number *")
    
    with col2:
        st.markdown("### Reservation Details")
        date = st.date_input("Date *", min_value=datetime.now().date())
        time = st.selectbox("Time *", BOOKING_SLOTS)
        party_size = st.number_input("Party Size *", min_value=1, max_value=12, value=2)
    
    special_requests = st.text_area("Special Requests (Optional)", placeholder="Dietary restrictions, celebrations, etc.")
    
    if st.button("🎉 Confirm Reservation", use_container_width=True):
        if name and email and phone:
            result = st.session_state.booking_system.create_booking(
                customer_name=name,
                email=email,
                phone=phone,
                date=str(date),
                time=time,
                party_size=party_size,
                special_requests=special_requests
            )
            
            if result["success"]:
                st.success(f"✅ {result['message']}")
                st.balloons()
            else:
                st.error(f"❌ {result['message']}")
        else:
            st.warning("⚠️ Please fill in all required fields.")
    
    # Show available slots
    st.markdown("---")
    st.markdown("### 📊 Available Time Slots")
    if st.button("Check Availability"):
        slots = st.session_state.booking_system.get_available_slots(str(date))
        if slots:
            df = pd.DataFrame(slots)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("All slots are fully booked for this date.")

def show_menu_page():
    st.markdown("## 🍽️ Our Menu")
    
    # Category tabs
    categories = list(MENU_DATA.keys())
    selected_category = st.selectbox("Select Category", categories)
    
    # Display menu items
    items = MENU_DATA[selected_category]
    
    cols = st.columns(2)
    for idx, item in enumerate(items):
        with cols[idx % 2]:
            st.markdown(f"""
                <div class="menu-card">
                    <div class="menu-item-name">{item['name']} {'⭐' if item.get('popular') else ''} {'👨‍🍳' if item.get('chef_special') else ''}</div>
                    <div class="menu-item-price">${item['price']}</div>
                    <p style="color: #666; margin-top: 0.5rem;">{item['description']}</p>
                    {f"<p style='color: #667eea; font-size: 0.9rem;'>🌱 {', '.join(item['dietary'])}</p>" if item.get('dietary') else ""}
                </div>
            """, unsafe_allow_html=True)

def show_info_page():
    st.markdown("## ℹ️ Restaurant Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
            <div class="info-box">
                <h3>📍 Location</h3>
                <p>{RESTAURANT_INFO['address']}</p>
                <h3>📞 Contact</h3>
                <p>Phone: {RESTAURANT_INFO['phone']}</p>
                <p>Email: {RESTAURANT_INFO['email']}</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="info-box">
                <h3>🕐 Operating Hours</h3>
        """, unsafe_allow_html=True)
        
        for day, hours in RESTAURANT_INFO['hours'].items():
            st.markdown(f"<p>{day}: {hours}</p>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Special offers
    st.markdown("### 🎁 Special Offers")
    for offer in SPECIAL_OFFERS:
        st.markdown(f"""
            <div class="info-box">
                <h4>{offer['name']}</h4>
                <p>{offer['description']}</p>
                <p><strong>Time:</strong> {offer['time']}</p>
                {f"<p><strong>Price:</strong> {offer['price']}</p>" if 'price' in offer else ""}
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
