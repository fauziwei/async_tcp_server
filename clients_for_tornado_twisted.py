# fauziwei@yahoo.com

import sys
import select
import socket

class Connection:
	def __init__(self):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			self.s.connect(('127.0.0.1', 1515))
			self.s.setblocking(True)
		except socket.error:
			self.s.close()
			print ( 'Socket error')
			sys.exit()

	def send(self):
		m = 'Hello, Im client\n'
		print ( 'Send: {}'.format(m) )
		self.s.send( m.encode('utf-8') )

	def recv(self):
		timeout = 15
		ready = select.select([self.s], [], [], timeout)
		try:
			if not ready[0]:
				self.s.close()
				print ( 'Recv > timeout {}'.format(timeout) )
			else:
				try:
					buffer = 25
					recv = self.s.recv(buffer)
				except socket.error:
					self.s.close()
					print ( 'Recv Failed' )
				print ( 'Recv: {}'.format(recv.decode('utf-8')) )
		except socket.error:
			self.s.close()
		finally: pass

	def call(self):
		self.send()
		self.recv()

	def run(self):
		# calls = [self.call() for i in range(100000)]
		# i = iter(calls)
		# while True:
		# 	try:
		# 		next(i)
		# 	except StopIteration:
		# 		break

		calls = (self.call() for i in range(100000))
		for i in calls:
			pass


c = Connection()
c.run()