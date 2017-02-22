# fauziwei@yahoo.com

from tornado import concurrent, ioloop, tcpserver, gen, iostream
# pip install futures
# from concurrent import futures

# with thread_pool
# 0.000124931335449

# without thread_pool
# 4.60147857666e-05
# 0.00046

thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

class Protocol:
	_clients = set()

	def __init__(self, stream, address):
		self._stream = stream
		self._address = address
		self.delimiter = '\n'
		self._stream.set_close_callback(self.on_close)
		# self.read_stream()

	def on_close(self):
		print ('{} close connection'.format(self._address[0]))
		Protocol._clients.discard(self)
		# self._stream.close()

	# def future_sleep(self, duration):
	# 	f = concurrent.Future()
	# 	ioloop.IOLoop.current().call_later(duration, lambda: f.set_result(None))
	# 	return f


	# def read_stream(self):
	# 	self._stream.read_until(self.delimiter, self.on_connect)

	# def on_connect(self, data):
	# 	try:
	# 		while True:
	# 			print ('Received: {}'.format(repr(data)))
	# 			s = self.long_pool(data)
	# 			self.send_stream(s)
	# 	except iostream.StreamClosedError: pass

	@gen.coroutine
	def on_connect(self):
		try:
			while True:
				data = yield self._stream.read_until(self.delimiter)
				data = data.replace(self.delimiter, '')
				print ('Received: {}'.format(repr(data)))
				# s = self.long_pool(data)
				# self.send_stream(s)

				# alternative future
				future = thread_pool.submit(self.long_pool, data)
				ioloop.IOLoop.current().add_future(future, self.send_stream_future)

				# alternative callback
				# future = thread_pool.submit(self.long_pool, data)
				# ioloop.IOLoop.current().add_callback(self.send_stream_future, future)				

		except iostream.StreamClosedError: pass

	def send_stream(self, data):
		print ('Send: {}'.format(repr(data)))
		self._stream.write('{}'.format(data))

	def send_stream_future(self, future):
		data = future.result()
		print ('Send: {}'.format(data))
		self._stream.write('Send: {}'.format(repr(data)))

	def long_pool(self, data):
		return 'Hello Im server'


class Factory(tcpserver.TCPServer):
	def handle_stream(self, stream, address):
		o = Protocol(stream, address)
		o.on_connect()
		# o.read_stream()

host, port = '127.0.0.1', 1515
Factory().listen(port, host)
ioloop.IOLoop.current().start()
