### Explicação do Fluxo

- **Usuário (Terminal, Web, Desktop)** → pode interagir de três formas diferentes.  
- **Core** → contém a lógica principal do chatbot (fixo, TF-IDF ou Gemini).  
- **Server** → hospeda o chatbot via navegador, com ou sem SSL, e usa `api_routes.py` para organizar endpoints.  
- **GUI** → interface desktop com PyQt5, conectada ao Gemini.  
- **Utils** → fornece funções auxiliares (pré-processamento de texto e configuração de variáveis).  
- **Main** → ponto de entrada que permite escolher qual versão rodar.  

---

### 📖 Passo a passo do que foi feito

1. **Protótipo inicial (`chatbot_basic.py`)**  
   - Criado um chatbot simples com respostas fixas em dicionário.  
   - Serve como base para evoluir para versões mais inteligentes.  

2. **Versão local (`qa_local.py`)**  
   - Implementado TF-IDF + similaridade de cosseno para encontrar respostas em uma base de perguntas/respostas.  
   - Adicionada lógica de limiar de similaridade para evitar respostas irrelevantes.  

3. **Integração com Gemini (`chatbot_ai.py`)**  
   - Conectado ao modelo Google Gemini via API.  
   - Criada classe `ChatbotAI` para encapsular chamadas ao modelo.  

4. **Servidores Web (`server_basic.py`, `server_ssl.py`, `api_routes.py`)**  
   - `server_basic.py`: servidor HTTP simples com interface HTML.  
   - `server_ssl.py`: servidor com SSL e autenticação básica.  
   - `api_routes.py`: centralização da lógica dos endpoints.  

5. **Interface Desktop (`chat_gui.py`)**  
   - Criada interface gráfica com PyQt5.  
   - Permite interação direta com o modelo Gemini.  

6. **Utilitários (`preprocessing.py`, `config.py`)**  
   - `preprocessing.py`: funções de limpeza e tokenização de texto.  
   - `config.py`: carrega variáveis de ambiente (API key, portas).  

7. **Ponto de entrada (`main.py`)**  
   - Criado script principal que permite escolher entre rodar a versão básica ou AI via argumentos de linha de comando.  
