import dotenv
from http import server

import request_handler

def main():
	dotenv.load_dotenv()
	handler = server.HTTPServer(('localhost', 8000), request_handler.RequestHandler)
	handler.serve_forever()
	handler.server_close()


if __name__ == '__main__':
	main()