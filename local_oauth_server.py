import http.server
import socketserver

PORT = 8888

class OAuthHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/callback'):
            # handle callback logic here
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Callback successful!')
        else:
            # serve other requests as usual
            super().do_GET()

with socketserver.TCPServer(("", PORT), OAuthHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

# To stop the server, use httpd.shutdown()