import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Application Settings
APP_TITLE = "🍽️ Bella Vista Restaurant"
APP_SUBTITLE = "Your AI-Powered Dining Assistant"

# Restaurant Information
RESTAURANT_INFO = {
    "name": "Bella Vista Restaurant",
    "address": "123 Gourmet Street, Food District, City 12345",
    "phone": "+1 (555) 123-4567",
    "email": "info@bellavista.com",
    "hours": {
        "Monday-Thursday": "11:00 AM - 10:00 PM",
        "Friday-Saturday": "11:00 AM - 11:00 PM",
        "Sunday": "10:00 AM - 9:00 PM"
    },
    "capacity": 100,
    "cuisine_type": "Italian-Mediterranean Fusion"
}

# Booking Configuration
BOOKING_SLOTS = [
    "11:00 AM", "11:30 AM", "12:00 PM", "12:30 PM",
    "1:00 PM", "1:30 PM", "2:00 PM", "2:30 PM",
    "5:00 PM", "5:30 PM", "6:00 PM", "6:30 PM",
    "7:00 PM", "7:30 PM", "8:00 PM", "8:30 PM",
    "9:00 PM", "9:30 PM", "10:00 PM"
]

MAX_PARTY_SIZE = 12
MIN_PARTY_SIZE = 1

# Database
DB_NAME = "restaurant_bookings.db"
