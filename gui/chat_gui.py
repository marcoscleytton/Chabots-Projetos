import sys
import google.generativeai as genai
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-1.5-pro-latest")
chat = model.start_chat(history=[])

class ChatbotApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Chatbot com Google AI')
        self.setGeometry(100, 100, 500, 400)

        layout = QVBoxLayout()
        self.chat_box = QTextEdit(self); self.chat_box.setReadOnly(True); layout.addWidget(self.chat_box)
        self.input_box = QLineEdit(self); layout.addWidget(self.input_box)
        self.send_button = QPushButton('Enviar', self); self.send_button.clicked.connect(self.enviar_pergunta); layout.addWidget(self.send_button)

        container = QWidget(); container.setLayout(layout); self.setCentralWidget(container)

    def enviar_pergunta(self):
        pergunta_usuario = self.input_box.text()
        if pergunta_usuario.lower() == 'fim': self.close()
        else:
            response = chat.send_message(pergunta_usuario)
            self.chat_box.append("Você: " + pergunta_usuario)
            self.chat_box.append("Chatbot: " + response.text)
            self.input_box.clear()

def main():
    app = QApplication(sys.argv)
    chatbot = ChatbotApp()
    chatbot.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()