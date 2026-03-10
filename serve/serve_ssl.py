import http.server, ssl, json
from http import HTTPStatus
from base64 import b64decode
from core.chatbot_ai import ChatbotAI
import os

chatbot = ChatbotAI(api_key=os.getenv("GOOGLE_API_KEY"))

class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    def authenticate(self):
        auth_header = self.headers.get('Authorization')
        if auth_header:
            try:
                auth_type, credentials = auth_header.split()
                if auth_type.lower() == 'basic':
                    decoded = b64decode(credentials).decode('utf-8')
                    username, password = decoded.split(':')
                    return username == "user1" and password == "password1"
            except Exception:
                return False
        return False

    def do_POST(self):
        if self.path == '/api/message':
            if not self.authenticate():
                self.send_response(HTTPStatus.UNAUTHORIZED)
                self.end_headers()
                return
            length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(length)
            user_input = json.loads(post_data).get('message', '')
            response_message = chatbot.get_response(user_input)
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'response': response_message}).encode())

def run():
    server_address = ('', 8443)
    httpd = http.server.HTTPServer(server_address, MyRequestHandler)
    httpd.socket = ssl.wrap_socket(httpd.socket,
                                   keyfile='path/to/server-key.pem',
                                   certfile='path/to/server-cert.pem',
                                   server_side=True)
    print("Servidor SSL rodando em https://localhost:8443")
    httpd.serve_forever()

if __name__ == "__main__":
    run()