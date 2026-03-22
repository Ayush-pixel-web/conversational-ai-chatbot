import random
from datetime import datetime

class MockChatbot:
    def __init__(self):
        self.conversation_history = []
        self.responses = {
            "hello": ["Hi there! How can I help you?", "Hello! Nice to meet you.", "Hey! What's up?"],
            "hi": ["Hi! How are you?", "Hello! What can I do for you?", "Hey there!"],
            "how are you": ["I'm doing great, thanks for asking!", "I'm fantastic! How about you?", "I'm here and ready to help!"],
            "what is your name": ["I'm MockBot, your conversational AI!", "You can call me MockBot.", "I'm MockBot, nice to meet you!"],
            "bye": ["Goodbye! Have a great day!", "See you later!", "Bye! Come back soon!"],
            "help": ["I'm here to chat with you! You can ask me anything.", "I can chat about pretty much anything. What's on your mind?", "Feel free to ask me questions or just chat!"],
            "thank you": ["You're welcome!", "Happy to help!", "Anytime!"],
            "thanks": ["You're welcome!", "My pleasure!", "Glad I could help!"],
        }
        
        self.default_responses = [
            "That's interesting! Tell me more.",
            "I see! Can you elaborate?",
            "That sounds cool! What else?",
            "Got it! Anything else?",
            "I hear you! What do you think about that?",
            "Interesting point! I agree.",
            "That makes sense to me!",
            "I understand! Keep going.",
            "Oh, I see! That's interesting.",
            "Tell me more about that!",
        ]

    def get_response(self, user_message: str) -> str:
        """Generate a response based on user input"""
        
        # Convert to lowercase for matching
        message_lower = user_message.lower().strip()
        
        # Check for keyword matches
        for keyword, responses in self.responses.items():
            if keyword in message_lower:
                return random.choice(responses)
        
        # If no keyword match, return a default response
        return random.choice(self.default_responses)

    def chat(self, user_message: str) -> dict:
        """Process user message and return response"""
        
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message,
            "timestamp": datetime.now().isoformat()
        })
        
        # Get bot response
        bot_response = self.get_response(user_message)
        
        # Add bot response to history
        self.conversation_history.append({
            "role": "bot",
            "content": bot_response,
            "timestamp": datetime.now().isoformat()
        })
        
        return {
            "user_message": user_message,
            "bot_response": bot_response,
            "timestamp": datetime.now().isoformat()
        }

    def get_history(self) -> list:
        """Return conversation history"""
        return self.conversation_history

    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
self.responses = {
    "hello": ["Hi there!", "Hello!"],
    "your_keyword": ["Response 1", "Response 2"],
    # Add more keywords and responses
}
