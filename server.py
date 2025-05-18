from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
    
        print(f"Requested path: {self.path}")
        # Check the requested path and respond accordingly
        # You can add more paths and their corresponding responses here

        if self.path == "/json":
            
            self.send_response(200) # 200 means "OK"
            # Define response headers
            self.send_header("Content-type", "application/json")
            self.end_headers()
            # Response body
            self.wfile.write(b'{"message": "Hello, JSON!"}')

        elif self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Welcome to my simple web server!")
            
        elif self.path == "/xml":
            self.send_response(200)
            self.send_header("Content-type", "application/xml")
            self.end_headers()
            self.wfile.write(b"<message>Hello, XML!</message>")
            
        elif self.path == "/csv":
            self.send_response(200)
            self.send_header("Content-type", "text/csv")
            self.end_headers()
            self.wfile.write(b"message,Hello, CSV")
            
        elif self.path == "/html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<html><body><h1>Hello, HTML!</h1></body></html>")
            
        elif self.path == "/javascript":
            self.send_response(200)
            self.send_header("Content-type", "application/javascript")
            self.end_headers()
            self.wfile.write(b"console.log('Hello, JavaScript!');")
            
        elif self.path == "/jpeg":
            try:
                # Read a JPEG file from disk
                with open("example.jpg", "rb") as f:
                    image_data = f.read()
                self.send_response(200)
                self.send_header("Content-type", "image/jpeg")
                self.end_headers()
                self.wfile.write(image_data)
            except FileNotFoundError:
                # Handle case where the file is missing
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"404 Image Not Found")
            
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")            
            
 
host = "localhost"
port = 8080
server = HTTPServer((host, port), SimpleHandler)

print(f"Server is running on http://{host}:{port}")
server.serve_forever()