import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "YOUR_API_KEY")
SERVER_PORT = int(os.getenv("SERVER_PORT", 8080))
SSL_PORT = int(os.getenv("SSL_PORT", 8443))