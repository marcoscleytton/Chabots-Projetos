import json
from core.chatbot_ai import ChatbotAI
import os

chatbot = ChatbotAI(api_key=os.getenv("GOOGLE_API_KEY"))

def handle_message(data):
    """Recebe JSON com 'message' e retorna resposta do chatbot."""
    user_input = data.get('message', '')
    response_message = chatbot.get_response(user_input)
    return {'response': response_message}

def health_check():
    """Endpoint simples para verificar se o servidor está ativo."""
    return {'status': 'ok'}