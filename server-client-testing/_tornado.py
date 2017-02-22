# Tornado
import time
from tornado import ioloop, tcpserver, iostream, gen, concurrent
mainloop = ioloop.IOLoop.current()

thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=1)

dtime = list()

class Protocol:
	__slots__ = ('stream', 'address')
	delimiter = '\n'

	def __init__(self, stream, address):
		self.stream = stream
		self.stream.set_close_callback(self.connectionLost)

	def connectionLost(self):
		print ( 'lost connection.')
		f = open('tornado.txt', 'w')
		for t in dtime:
			f.write('{0:.6f} '.format(t))
		f.close()

	@gen.coroutine
	def lineReceived(self):
		try:
			while True:
				self.dt = time.time()
				s = yield self.stream.read_until(self.delimiter)
				s = s.replace('\n', '')
				print ('Recv: {}'.format(s))

				future = thread_pool.submit(Protocol.longPolling, s)
				# mainloop.add_future(future, self.sendStream)
				future.add_done_callback(lambda future: mainloop.add_callback(self.sendStream))

		except iostream.StreamClosedError:
			pass

	def sendStream(self, future):
		s = future.result()
		print ( 'Send: {}'.format(s.replace('client', 'server')))
		self.stream.write(s.replace('client', 'server'))
		stop = time.time() - self.dt
		dtime.append(stop)

	@staticmethod
	def longPolling(s):
		return s

class Factory(tcpserver.TCPServer):
	def handle_stream(self, stream, address):
		o = Protocol(stream, address)
		o.lineReceived()

host, port = 'localhost', 1516
reactor = Factory()
reactor.listen(port, host)
mainloop.start()
