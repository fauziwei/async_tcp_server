from tornado.web import RequestHandler, \
						Application as _Application
from tornado.ioloop import IOLoop

class ReverseHandler(RequestHandler):
	def get(self, input):
		result = input
		self.write(result[::-1])

app = _Application(
	handlers = [
		#http://localhost:8000/reverse/opoaeiki
		(r'/reverse/(\w+)', ReverseHandler),
	]
)

app.listen(8000)
IOLoop.instance().start()