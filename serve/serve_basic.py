import http.server, json
from core.chatbot_ai import ChatbotAI

chatbot = ChatbotAI(api_key="YOUR_API_KEY")

class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.render_html().encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/api/message':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            user_input = json.loads(post_data).get('message', '')
            response_message = chatbot.get_response(user_input)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'response': response_message}).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def render_html(self):
        return """<!DOCTYPE html>
        <html><body>
        <h2>Chatbot</h2>
        <div id="messages"></div>
        <input id="user-input"/><button onclick="sendMessage()">Enviar</button>
        <script>
        function sendMessage(){
            const userInput=document.getElementById('user-input').value;
            fetch('/api/message',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:userInput})})
            .then(r=>r.json()).then(d=>{
                document.getElementById('messages').innerHTML+="<p><b>Você:</b> "+userInput+"</p><p><b>Bot:</b> "+d.response+"</p>";
            });
        }
        </script></body></html>"""