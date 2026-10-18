import json
import sys
import threading
import unittest
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
import server


class ServerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.httpd = server.make_server(0)
        cls.port = cls.httpd.server_address[1]
        cls.thread = threading.Thread(target=cls.httpd.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()

    def get(self, path):
        url = f"http://127.0.0.1:{self.port}{path}"
        return urllib.request.urlopen(url, timeout=3)

    def test_root(self):
        resp = self.get("/")
        self.assertEqual(resp.status, 200)
        self.assertIn("Hello", resp.read().decode())

    def test_healthz(self):
        resp = self.get("/healthz")
        self.assertEqual(resp.status, 200)
        self.assertEqual(resp.read().decode().strip(), "ok")

    def test_notes(self):
        resp = self.get("/notes")
        data = json.loads(resp.read().decode())
        self.assertEqual(data["count"], 4)
