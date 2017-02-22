# fauziwei@yahoo.com

import time
from tornado import ioloop
from tornado import web
from tornado import gen

class Index(web.RequestHandler):
	@gen.coroutine
	def get(self):
		print ('start')
		yield self.async_proc(2)
		print ('end')
		print ('im tiring')
		self.finish()

	@gen.coroutine
	def async_proc(self, timeout):
		''' sleep without blocking '''
		yield gen.Task(ioloop.IOLoop.instance().add_timeout, time.time()+timeout)


class Application(web.Application):
	def __init__(self):
		apis = [
			(r'/', Index)
		]
		settings = dict( debug=False )
		web.Application.__init__(self, apis, **settings)

app = Application()

host, port = 'localhost', 8080
app.listen(port, host)
ioloop.IOLoop.instance().start()
