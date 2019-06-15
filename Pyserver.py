import http.server 
import socketserver 
IP="127.0.0.1"
PORT = 8080 
Handler = http.server.SimpleHTTPRequestHandler 
with socketserver.TCPServer((IP, PORT), Handler) as httpd: 
	print("serving at port", PORT) 
	httpd.serve_forever()




http.server.close()
