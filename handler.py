import json
import http.server
import socketserver
import json
import argparse
# def handler(event, context):
# 	return "hello world"
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/version':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            version = {
                "server_version": "4.0.0",            }
            self.wfile.write(json.dumps(version).encode('utf-8'))
        else:
            self.send_error(404, "Not Found")

def handler(event, context):
    port = int(context.function.port)
    with socketserver.TCPServer(("", port), MyRequestHandler) as httpd:
        print(f"Serving on port {port}")
        httpd.serve_forever()