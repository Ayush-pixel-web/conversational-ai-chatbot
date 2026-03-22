const API_URL = 'http://localhost:8000';

// DOM Elements
const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');
const chatMessages = document.getElementById('chatMessages');

// Event listeners
sendButton.addEventListener('click', sendMessage);
messageInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

async function sendMessage() {
    const message = messageInput.value.trim();
    
    if (!message) {
        alert('Please enter a message');
        return;
    }

    // Add user message to chat
    addMessageToChat(message, 'user');
    
    // Clear input
    messageInput.value = '';
    messageInput.focus();
    
    try {
        // Send message to backend
        const response = await fetch(`${API_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        });

        if (!response.ok) {
            throw new Error('Failed to get response from server');
        }

        const data = await response.json();
        
        // Add bot response to chat
        addMessageToChat(data.bot_response, 'bot');
        
    } catch (error) {
        console.error('Error:', error);
        addMessageToChat('Sorry, I encountered an error. Please try again.', 'bot');
    }
}

function addMessageToChat(message, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;
    
    const paragraph = document.createElement('p');
    paragraph.textContent = message;
    
    messageDiv.appendChild(paragraph);
    chatMessages.appendChild(messageDiv);
    
    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

async function clearChat() {
    if (confirm('Are you sure you want to clear the chat?')) {
        try {
            const response = await fetch(`${API_URL}/clear`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                }
            });

            if (response.ok) {
                chatMessages.innerHTML = '';
                addMessageToChat('Chat cleared! Let\'s start fresh.', 'bot');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Failed to clear chat');
        }
    }
}

async function showHistory() {
    try {
        const response = await fetch(`${API_URL}/history`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            }
        });

        if (!response.ok) {
            throw new Error('Failed to get history');
        }

        const data = await response.json();
        const history = data.history;

        if (history.length === 0) {
            alert('No conversation history yet');
            return;
        }

        // Format and display history
        let historyText = 'Conversation History:\n\n';
        history.forEach((msg, index) => {
            historyText += `${index + 1}. [${msg.role.toUpperCase()}]: ${msg.content}\n`;
        });

        console.log(historyText);
        alert(historyText);

    } catch (error) {
        console.error('Error:', error);
        alert('Failed to retrieve history');
    }
}

// Check if API is available on page load
window.addEventListener('load', async () => {
    try {
        const response = await fetch(`${API_URL}/health`);
        if (!response.ok) {
            throw new Error('API not available');
        }
        console.log('✓ Connected to chatbot API');
    } catch (error) {
        console.error('⚠️ Warning: Could not connect to backend API');
        console.error('Make sure the backend is running on http://localhost:8000');
        addMessageToChat('⚠️ Backend not connected. Make sure to run: python -m uvicorn main:app --reload', 'bot');
    }
});
