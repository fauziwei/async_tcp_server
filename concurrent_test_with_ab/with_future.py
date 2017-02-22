from tornado import gen
from tornado.concurrent import Future
from tornado.web import RequestHandler, \
						Application as _Application
from tornado.ioloop import IOLoop

class ReverseHandler(RequestHandler):
	@gen.coroutine
	def get(self, input):
		#future = Future()
		#future.set_result(input)
		#result = yield future
		#self.write(result[::-1])
		result = yield self.f(input)
		self.write(result)

	@gen.coroutine
	def f(i):
		r = i[::-1]
		raise gen.Return(r)

app = _Application(
	handlers = [
		#http://localhost:8000/reverse/opoaeiki
		(r'/reverse/(\w+)', ReverseHandler),
	]
)

app.listen(8000)
IOLoop.instance().start()