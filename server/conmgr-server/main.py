import http.server

import handler

PORT = 8000

Handler = handler.ConmgrHTTPRequestHandler

try:
    httpd = http.server.HTTPServer(("", PORT), Handler)
    print("serving at port", PORT)
    httpd.serve_forever()
except KeyboardInterrupt:
    print('^C received, shutting down server')
    httpd.socket.close()
