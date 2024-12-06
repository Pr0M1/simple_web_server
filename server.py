from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHandler(BaseHTTPRequestHandler):
    def do_get(self):

host = "localhost"
port = 8080