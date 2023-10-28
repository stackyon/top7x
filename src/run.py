from http import server

import request_handler


handler = server.HTTPServer(('localhost', 8000), request_handler.RequestHandler)
handler.serve_forever()
handler.server_close()