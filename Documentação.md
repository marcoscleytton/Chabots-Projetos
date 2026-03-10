# Documentação do Projeto Chatbot

Este projeto reúne diferentes versões de um **chatbot em Python**, desde a versão mais simples até integrações avançadas com **Google Gemini AI**, além de interfaces **web** e **desktop (PyQt5)**.

---

## Estrutura do Projeto

```markdown
chatbot_project/
│
├── core/                  # Núcleo da lógica do chatbot
│   ├── chatbot_basic.py   # Chatbot simples com respostas fixas
│   ├── qa_local.py        # Chatbot com TF-IDF e similaridade de cosseno
│   └── chatbot_ai.py      # Chatbot integrado ao Google Gemini
│
├── server/                # Servidores web
│   ├── server_basic.py    # Servidor HTTP com interface web simples
│   ├── server_ssl.py      # Servidor HTTP com SSL e autenticação básica
│   └── api_routes.py      # Organização dos endpoints (funções auxiliares)
│
├── gui/                   # Interfaces gráficas
│   └── chat_gui.py        # Interface desktop com PyQt5
│
├── utils/                 # Utilitários e configurações
│   ├── preprocessing.py   # Funções de limpeza e tokenização de texto
│   └── config.py          # Configurações e variáveis de ambiente
│
└── main.py                # Ponto de entrada principal
```

---

##  Documentação por pasta

### 1. `core/`
Contém a lógica principal do chatbot em diferentes versões:
- **`chatbot_basic.py`** → chatbot simples com respostas fixas (protótipo inicial).
- **`qa_local.py`** → chatbot que usa **TF-IDF + similaridade de cosseno** para encontrar respostas em uma base local.
- **`chatbot_ai.py`** → integração com **Google Gemini AI**, permitindo respostas inteligentes e dinâmicas.

> Use esta pasta para escolher qual versão do chatbot você quer rodar.

---

### 2. `server/`
Contém servidores web para rodar o chatbot via navegador:
- **`server_basic.py`** → servidor HTTP simples, renderiza uma página HTML com chat.
- **`server_ssl.py`** → servidor com **SSL e autenticação básica** (usuário/senha).
- **`api_routes.py`** → centraliza funções auxiliares de endpoints (ex.: `/api/message`, health check).

> Use esta pasta para disponibilizar o chatbot como serviço web.

---

### 3. `gui/`
Contém interfaces gráficas:
- **`chat_gui.py`** → interface desktop feita com **PyQt5**, permitindo interação direta com o modelo Gemini.

> Use esta pasta para rodar o chatbot em modo gráfico no computador.

---

### 4. `utils/`
Contém utilitários e configurações:
- **`preprocessing.py`** → funções de limpeza de texto (remoção de pontuação, normalização, tokenização).
- **`config.py`** → carrega variáveis de ambiente (como `GOOGLE_API_KEY`, portas do servidor, etc.).

> Use esta pasta para centralizar configurações e funções auxiliares.

---

### 5. `main.py`
Ponto de entrada principal do projeto.  
Permite escolher qual versão rodar via **argumentos de linha de comando**:

```bash
python main.py --mode basic   # Chatbot simples
python main.py --mode ai      # Chatbot com Google Gemini
```

---

##  Passo a passo para utilizar

1. **Instalar dependências**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configurar chave da API**
   - Crie um arquivo `.env` na raiz do projeto:
     ```
     GOOGLE_API_KEY=sua_chave_aqui
     SERVER_PORT=8080
     SSL_PORT=8443
     ```

3. **Rodar versões**
   - **Terminal (básico)**:
     ```bash
     python core/chatbot_basic.py
     ```
   - **Terminal (AI Gemini)**:
     ```bash
     python main.py --mode ai
     ```
   - **Web (HTTP)**:
     ```bash
     python server/server_basic.py
     ```
     Acesse: `http://localhost:8080`
   - **Web (SSL + autenticação)**:
     ```bash
     python server/server_ssl.py
     ```
     Acesse: `https://localhost:8443`
   - **Desktop (PyQt5)**:
     ```bash
     python gui/chat_gui.py
     ```

---

## Fluxo do Projeto (Mapa de Módulos)

```markdown
Usuário
 │
 ├── (Terminal) → core/chatbot_basic.py
 │                 core/qa_local.py
 │                 core/chatbot_ai.py
 │
 ├── (Web) → server/server_basic.py → api_routes.py → core/chatbot_ai.py
 │           server/server_ssl.py   → api_routes.py → core/chatbot_ai.py
 │
 └── (Desktop) → gui/chat_gui.py → core/chatbot_ai.py
```
Quer que eu prepare também um **diagrama visual em Mermaid (Markdown)** para ilustrar graficamente esse fluxo de módulos dentro do README?
