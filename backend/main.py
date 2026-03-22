from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot import MockChatbot

# Initialize FastAPI app
app = FastAPI(title="Conversational AI Chatbot", version="1.0.0")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize chatbot
chatbot = MockChatbot()

# Request/Response models
class MessageRequest(BaseModel):
    message: str

class MessageResponse(BaseModel):
    user_message: str
    bot_response: str
    timestamp: str

class HistoryResponse(BaseModel):
    history: list

# Routes
@app.get("/")
def root():
    """Health check endpoint"""
    return {"status": "ok", "message": "Chatbot API is running!"}

@app.post("/chat", response_model=MessageResponse)
def chat(request: MessageRequest):
    """Chat endpoint - send a message and get a response"""
    response = chatbot.chat(request.message)
    return MessageResponse(**response)

@app.get("/history", response_model=HistoryResponse)
def get_history():
    """Get conversation history"""
    return HistoryResponse(history=chatbot.get_history())

@app.post("/clear")
def clear_history():
    """Clear conversation history"""
    chatbot.clear_history()
    return {"status": "success", "message": "Conversation history cleared"}

@app.get("/health")
def health():
    """Health check"""
    return {"status": "healthy", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
