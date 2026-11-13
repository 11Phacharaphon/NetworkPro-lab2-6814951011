from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse
import json
import html


class SimpleServer(SimpleHTTPRequestHandler):
    def _send(self, code, body, content_type="text/html; charset=utf-8"):
        data = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        # แยกพารามิเตอร์จาก URL เช่น /?msg=hello
        parsed_path = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed_path.query)
        msg = params.get("msg", ["Hello, World! V2"])[0]
        print(f"[GET] path={self.path} msg={msg}", flush=True)
        self._send(200, f"<html><body><h1>{html.escape(msg)}</h1></body></html>")

    def do_POST(self):
        # อ่านข้อมูลที่ client ส่งมา (รองรับทั้ง JSON และ form-urlencoded)
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length).decode("utf-8")
        ctype = self.headers.get("Content-Type", "")

        if "application/json" in ctype:
            try:
                data = json.loads(raw) if raw else {}
            except json.JSONDecodeError:
                self._send(400, json.dumps({"error": "invalid JSON"}), "application/json")
                return
        else:
            data = {k: v[0] for k, v in urllib.parse.parse_qs(raw).items()}

        print(f"[POST] path={self.path} data={data}", flush=True)
        response = {"status": "received", "method": "POST", "received_data": data}
        self._send(200, json.dumps(response, ensure_ascii=False), "application/json; charset=utf-8")


if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SimpleServer)
    print("Server running on port 8000...", flush=True)
    httpd.serve_forever()
