from http import server


class RequestHandler(server.BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		self.wfile.write(bytes("hello wrld", 'utf-8'))

	def do_POST(self):
		pass