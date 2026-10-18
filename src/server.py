import json
import os
import signal
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

NOTES = ["buy milk", "learn docker", "write ci"]


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype="text/plain"):
        data = body.encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == "/":
            self._send(200, "Hello from notes service\n")
        elif self.path == "/healthz":
            self._send(200, "ok\n")
        elif self.path == "/notes":
            body = json.dumps({"count": len(NOTES), "notes": NOTES})
            self._send(200, body, "application/json")
        else:
            self._send(404, "not found\n")


def make_server(port):
    return ThreadingHTTPServer(("0.0.0.0", port), Handler)


def main():
    port = int(os.environ.get("PORT", "8080"))
    server = make_server(port)
    signal.signal(signal.SIGTERM, lambda signum, frame: sys.exit(0))
    print(f"listening on 0.0.0.0:{port}", flush=True)
    try:
        server.serve_forever()
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
