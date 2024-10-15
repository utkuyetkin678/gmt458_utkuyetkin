# server.py
import http.server
import socketserver

# Sunucunun çalışacağı port
PORT = 8010

# HTTP İsteklerini handle eden sınıf
Handler = http.server.SimpleHTTPRequestHandler

# Sunucuyu başlat
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
