from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        print("do_GET was called!")
        
        # Response code
        self.send_response(200) # 200 means "OK"

        # Define response headers
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        # Response body
        self.wfile.write(b"Hello, World!")


host = "localhost"
port = 8080
server = HTTPServer((host, port), SimpleHandler)

print(f"Server is running on http://{host}:{port}")
server.serve_forever()