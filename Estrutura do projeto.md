chatbot_project/
│
## core/   --               # Núcleo da lógica do chatbot
chatbot_basic.py   # Chatbot simples com respostas fixas
qa_local.py        # Chatbot com TF-IDF e similaridade de cosseno
chatbot_ai.py      # Chatbot integrado ao Google Gemini

## server/                # Servidores web
server_basic.py    # Servidor HTTP com interface web simples
server_ssl.py      # Servidor HTTP com SSL e autenticação básica
api_routes.py      # Organização dos endpoints (funções auxiliares)

##  gui/                   # Interfaces gráficas
chat_gui.py        # Interface desktop com PyQt5

##  utils/                 # Utilitários e configurações
preprocessing.py   # Funções de limpeza e tokenização de texto
config.py          # Configurações e variáveis de ambiente


## --  main.py                # Ponto de entrada principal
