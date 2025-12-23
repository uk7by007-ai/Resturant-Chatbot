# 🍽️ Bella Vista Restaurant - AI Chatbot

A comprehensive AI-powered restaurant chatbot with voice capabilities, intelligent booking system, and a stunning Streamlit interface.

## ✨ Features

- **🤖 AI Chatbot**: Powered by Google Gemini AI for intelligent conversations
- **🎤 Voice Input/Output**: Speak your questions and hear responses
- **📅 Smart Booking System**: Real-time reservation management with availability checking
- **🍽️ Complete Menu**: Browse our full menu with dietary information
- **💎 Premium UI**: Beautiful glassmorphic design with smooth animations
- **📊 Real-time Analytics**: View booking statistics and popular items

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Microphone (for voice features)
- Google Gemini API key

### Installation

1. **Clone or download this project**

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Set up your API key**:
   - The `.env` file is already configured with your Gemini API key
   - If you need to change it, edit the `.env` file

4. **Run the application**:
```bash
streamlit run app.py
```

5. **Open your browser**:
   - The app will automatically open at `http://localhost:8501`

## 📖 Usage Guide

### Chat Assistant
1. Navigate to "💬 Chat Assistant"
2. Type your questions or enable voice input
3. Ask about menu items, hours, dietary options, or recommendations
4. Get instant AI-powered responses

### Make Reservations
1. Go to "📅 Make Reservation"
2. Fill in your details (name, email, phone)
3. Select date, time, and party size
4. Add any special requests
5. Confirm your booking

### Voice Features
1. Enable "Voice Input" in the sidebar
2. Click "🎤 Listen" to speak your question
3. The AI will respond with both text and voice

### Browse Menu
1. Visit "🍽️ View Menu"
2. Select a category (Appetizers, Main Courses, Pasta, Desserts, Beverages)
3. View detailed descriptions, prices, and dietary information
4. Look for ⭐ (popular) and 👨‍🍳 (chef's special) indicators

## 🎨 Features Breakdown

### AI Chatbot
- Natural language understanding
- Context-aware conversations
- Menu recommendations
- Dietary restriction assistance
- Restaurant information

### Booking System
- SQLite database for reservations
- Real-time availability checking
- Capacity management (100 guests)
- Email and phone validation
- Special requests handling

### Voice Capabilities
- Speech-to-text using Google Speech Recognition
- Text-to-speech using gTTS
- Automatic audio playback
- Error handling for unclear speech

### Premium UI
- Glassmorphic design
- Gradient backgrounds
- Smooth animations
- Responsive layout
- Custom color palette
- Google Fonts (Playfair Display, Inter)

## 📁 Project Structure

```
restaurant-chatbot/
├── app.py                  # Main Streamlit application
├── chatbot_engine.py       # AI chatbot logic
├── booking_system.py       # Reservation management
├── voice_handler.py        # Speech recognition & TTS
├── restaurant_data.py      # Menu and restaurant info
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
└── README.md             # This file
```

## 🔧 Configuration

### Restaurant Settings
Edit `config.py` to customize:
- Restaurant name and information
- Operating hours
- Booking time slots
- Maximum party size
- Restaurant capacity

### Menu Items
Edit `restaurant_data.py` to:
- Add/remove menu items
- Update prices
- Modify descriptions
- Set dietary information
- Mark popular items

## 🛠️ Troubleshooting

### Voice Input Not Working
- Ensure your microphone is connected
- Grant microphone permissions to your browser
- Check microphone settings in your OS

### API Errors
- Verify your Gemini API key is correct in `.env`
- Check your internet connection
- Ensure you haven't exceeded API rate limits

### Database Issues
- Delete `restaurant_bookings.db` to reset the database
- The database will be recreated automatically

## 🌟 Advanced Features

### Custom Styling
The app uses custom CSS for premium aesthetics:
- Glassmorphism effects
- Gradient backgrounds
- Smooth transitions
- Hover animations

### Database Management
- SQLite database for persistent storage
- Automatic table creation
- Booking history tracking
- Status management (confirmed/cancelled)

## 📝 Notes

- Voice features require an active internet connection
- The chatbot uses Google Gemini Pro model
- All bookings are stored locally in SQLite
- The app supports up to 100 concurrent guests

## 🎯 Future Enhancements

Potential improvements:
- Email confirmation for bookings
- SMS notifications
- Payment integration
- Multi-language support
- Customer reviews system
- Loyalty program

## 📞 Support

For issues or questions:
- Check the troubleshooting section
- Review the code comments
- Test with simple queries first

## 🙏 Credits

Built with:
- Streamlit
- Google Gemini AI
- SpeechRecognition
- gTTS
- SQLite

---

**Enjoy your premium restaurant chatbot experience! 🍽️✨**
