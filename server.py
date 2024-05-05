from http.server import BaseHTTPRequestHandler, HTTPServer

class RedirectHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(302)
        self.send_header('Location', 'http://10.0.2.2/applink')
        self.end_headers()

def run(server_class=HTTPServer, handler_class=RedirectHandler, port=8020):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server listening on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
