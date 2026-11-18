#!/usr/bin/env python3
"""Serve o frontend e repassa /regular/* e /simples/* para as APIs da Receita rodando local."""
import http.server, urllib.request, urllib.error, os, sys
DESTINOS = {'/regular/': 'http://127.0.0.1:8080/api/', '/simples/': 'http://127.0.0.1:8082/api/'}
AQUI = os.path.dirname(os.path.abspath(__file__))

class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k): super().__init__(*a, directory=AQUI, **k)
    def _proxy(self):
        for pre, dest in DESTINOS.items():
            if self.path.startswith(pre):
                url = dest + self.path[len(pre):]
                corpo = None
                if self.command == 'POST':
                    corpo = self.rfile.read(int(self.headers.get('Content-Length', 0)))
                req = urllib.request.Request(url, data=corpo, method=self.command,
                        headers={'Content-Type': 'application/json'})
                try:
                    r = urllib.request.urlopen(req, timeout=60); status, dados = r.status, r.read()
                except urllib.error.HTTPError as e: status, dados = e.code, e.read()
                except Exception as e:
                    status, dados = 502, ('{"erro":"API local fora do ar: %s"}' % e).encode()
                self.send_response(status); self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(dados))); self.end_headers(); self.wfile.write(dados)
                return True
        return False
    def do_GET(self):
        if not self._proxy(): super().do_GET()
    def do_POST(self):
        if not self._proxy(): self.send_error(404)
    def log_message(self, *a): pass

if __name__ == '__main__':
    porta = int(sys.argv[1]) if len(sys.argv) > 1 else 8090
    print('Explorador em http://localhost:%d' % porta)
    http.server.ThreadingHTTPServer(('0.0.0.0', porta), H).serve_forever()
