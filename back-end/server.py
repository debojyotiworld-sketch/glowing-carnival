import http.server
import json

counter = 0

def do_COUNT():
    global counter
    counter += 1
    return json.dumps({"count": counter})

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/counter':
            self.send_header()
            
    def do_GET(self):
        if self.path == '/api/counter':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(do_COUNT().encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"404 Not Found.")

(http.server.HTTPServer(('localhost', 8000), RequestHandler)).serve_forever()