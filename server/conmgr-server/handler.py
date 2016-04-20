import http.server
import json

import docker-ops

class ConmgrHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()
    def do_GET(self):
        print(self.path)
        if self.path == "/api/getContainers":
            containers = docker-ops.getContainers();

            self.send_response(200)
            self.send_header("Content-type", "text/json")
            self.end_headers()

            print(self.wfile)
            self.wfile.write("<html><head><title>Title goes here.</title></head>".encode("utf-8"))
            self.wfile.write("<body><p>This is a test.</p>".encode("utf-8"))
            self.wfile.write(("<p>You accessed path: %s</p>" % self.path).encode("utf-8"))
            self.wfile.write("</body></html>".encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/json")
            self.end_headers()

    def do_POST(self):
        print(self.path)
        if self.path == "/api/startContainer":
            body = json.load(self.rfile)
            docker-ops.startContainer()

            self.send_response(200)
            self.send_header("Content-type", "text/json")
            self.end_headers()
        else if self.path == "/api/stopContainer":
            body = json.load(self.rfile)
            docker-ops.stopContainer()
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/json")
            self.end_headers()
