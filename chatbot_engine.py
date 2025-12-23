"""
Chatbot Engine - AI-Powered Restaurant Assistant using Google Gemini
"""

import google.generativeai as genai
from config import GEMINI_API_KEY, RESTAURANT_INFO
from restaurant_data import get_full_menu_text, SPECIAL_OFFERS, DIETARY_INFO, CHEF_RECOMMENDATIONS

class RestaurantChatbot:
    def __init__(self):
        # Configure Gemini API
        genai.configure(api_key=GEMINI_API_KEY)
        
        # Initialize the model - using gemini-2.5-flash (confirmed available)
        self.model = genai.GenerativeModel('models/gemini-2.5-flash')
        
        # Conversation history
        self.chat_history = []
        
        # System context
        self.system_context = self._build_system_context()
        
        # Start chat session
        self.chat = self.model.start_chat(history=[])
    
    def _build_system_context(self):
        """Build comprehensive system context for the AI"""
        
        context = f"""You are an AI assistant for {RESTAURANT_INFO['name']}, a premium {RESTAURANT_INFO['cuisine_type']} restaurant.

RESTAURANT INFORMATION:
- Name: {RESTAURANT_INFO['name']}
- Address: {RESTAURANT_INFO['address']}
- Phone: {RESTAURANT_INFO['phone']}
- Email: {RESTAURANT_INFO['email']}

OPERATING HOURS:
"""
        for day, hours in RESTAURANT_INFO['hours'].items():
            context += f"- {day}: {hours}\n"
        
        context += f"\nCAPACITY: {RESTAURANT_INFO['capacity']} guests\n\n"
        
        # Add menu
        context += get_full_menu_text()
        
        # Add special offers
        context += "\n\nSPECIAL OFFERS:\n"
        for offer in SPECIAL_OFFERS:
            context += f"\n{offer['name']}: {offer['description']}\n"
            context += f"Time: {offer['time']}\n"
            if 'price' in offer:
                context += f"Price: {offer['price']}\n"
        
        # Add dietary info
        context += "\n\nDIETARY INFORMATION:\n"
        for key, value in DIETARY_INFO.items():
            context += f"- {key.title()}: {value}\n"
        
        # Add chef recommendations
        context += "\n\nCHEF'S RECOMMENDATIONS:\n"
        for rec in CHEF_RECOMMENDATIONS:
            context += f"- {rec}\n"
        
        context += """

YOUR ROLE:
You are a friendly, knowledgeable, and professional restaurant assistant. Your responsibilities include:
1. Answering questions about the menu, ingredients, and dishes
2. Providing recommendations based on customer preferences
3. Sharing information about restaurant hours, location, and policies
4. Assisting with dietary restrictions and allergies
5. Explaining special offers and promotions
6. Helping customers understand the booking process

GUIDELINES:
- Be warm, welcoming, and enthusiastic about the restaurant
- Provide detailed, accurate information from the menu and restaurant data
- If asked about bookings, guide users to use the booking system
- If you don't know something, be honest and offer to help in other ways
- Use emojis occasionally to be friendly (🍽️, 🍷, 👨‍🍳, ⭐)
- Keep responses concise but informative
- Always prioritize customer satisfaction

Remember: You represent a premium dining establishment. Maintain a professional yet friendly tone.
"""
        
        return context
    
    def get_response(self, user_message):
        """
        Get AI response to user message
        
        Args:
            user_message: User's input message
        
        Returns:
            AI-generated response
        """
        try:
            # For the first message, include system context
            if len(self.chat_history) == 0:
                full_message = f"{self.system_context}\n\nCustomer: {user_message}"
            else:
                full_message = user_message
            
            # Get response from Gemini
            response = self.chat.send_message(full_message)
            ai_response = response.text
            
            # Store in history
            self.chat_history.append({
                "role": "user",
                "content": user_message
            })
            self.chat_history.append({
                "role": "assistant",
                "content": ai_response
            })
            
            return ai_response
            
        except Exception as e:
            error_message = f"I apologize, but I'm having trouble processing your request. Error: {str(e)}"
            return error_message
    
    def reset_conversation(self):
        """Reset the conversation history"""
        self.chat_history = []
        self.chat = self.model.start_chat(history=[])
        return "Conversation reset. How can I help you today?"
    
    def get_chat_history(self):
        """Get the conversation history"""
        return self.chat_history
