import http.server
import json

import docker_ops

class ConmgrHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def send_response_ok(self):
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()
    def send_response_ok_nb(self):
        self.send_response(200)
        self.end_headers()
    def send_response_nf(self):
        self.send_response(404)
        self.end_headers()
    def send_response_br(self):
        self.send_response(400)
        self.end_headers()

    def parse_body(self):
        body_string = self.rfile.read(int(self.headers['Content-Length'])).decode("utf-8")
        try:
            body = json.loads(body_string)
            if 'id' in body:
                return body
            else:
                return None
        except json.JSONDecodeError:
            return None

    def do_HEAD(self):
        if self.path == "/api/getContainers":
            self.send_response_ok()
        else:
            self.send_response_nf()
    def do_GET(self):
        if self.path == "/api/getContainers":
            self.send_response_ok()
            self.wfile.write(json.JSONEncoder().encode(o=docker_ops.getContainers()).encode('utf-8'))
        else:
            self.send_response_nf()
    def do_POST(self):
        body = self.parse_body()
        if not body == None:
            if self.path == "/api/startContainer":
                if docker_ops.startContainer(body['id']):
                    self.send_response_ok_nb()
                else:
                    self.send_response_nf()
            elif self.path == "/api/stopContainer":
                if docker_ops.stopContainer(body['id']):
                    self.send_response_ok_nb()
                else:
                    self.send_response_nf()
            else:
                self.send_response_nf()
        else:
            self.send_response_br()
