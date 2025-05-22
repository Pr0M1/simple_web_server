import os
from urllib.parse import unquote
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):

        request_path = unquote(self.path)
        print(f"Requested path: {request_path}")

        # Handle root ("/") as index.html in static
        if request_path == "/" or request_path == "":
            file_path = os.path.join("static", "index.html")

        # If it starts with "/images/", serve from "images/"
        elif request_path.startswith("/images/"):
            file_path = request_path.lstrip("/")  # "images/example.jpg"

        # Otherwise, serve from "static" (CSS, JS, etc.)
        else:
            file_path = os.path.join("static", request_path.lstrip("/"))

        # Get the content type based on file extension
        content_types = {
            ".html": "text/html",
            ".css": "text/css",
            ".js": "application/javascript",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".png": "image/png",
            ".gif": "image/gif",
            ".json": "application/json",
            ".txt": "text/plain",
        }

        # Get extension and content-type
        _, ext = os.path.splitext(file_path)
        content_type = content_types.get(ext, "application/octet-stream")

        # Try to read and return the file
        try:
            with open(file_path, "rb") as f:
                content = f.read()
            self.send_response(200)
            self.send_header("Content-type", content_type)
            self.end_headers()
            self.wfile.write(content)
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")

         
host = "0.0.0.0"
port = 8080
server = HTTPServer((host, port), SimpleHandler)

print(f"Server is running on http://{host}:{port}")
server.serve_forever()