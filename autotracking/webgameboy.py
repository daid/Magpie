import socket
import consts
import http.server
import threading


class HttpRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(b'OK')

        if len(post_data) == 0x2080:
            WebGameboy.instance.ram[0:0x2000] = post_data[0:0x2000]
            WebGameboy.instance.ram[consts.hram - consts.wram:consts.hram - consts.wram + 0x80] = post_data[0x2000:0x2080]

    do_POST = do_GET


class WebGameboy:
    instance = None
    def __init__(self, port: int):
        self.ram = bytearray(consts.snapshotSize)
        self.canReadRom = False
        WebGameboy.instance = self

        self.server = http.server.HTTPServer(('127.0.0.1', 8010), HttpRequestHandler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

    def isConnected(self):
        return True

    def readSnapshot(self):
        return self.ram
