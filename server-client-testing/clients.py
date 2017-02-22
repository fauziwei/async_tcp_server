import sys
import select
import socket

class Kboom:
	def __init__(self):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			self.s.connect(('localhost', 1516))
			self.s.setblocking(1)
		except socket.error:
			self.s.close()

	def send(self):
		s = 'Hello Im client'
		print ('Send: {0}'.format(s))
		self.s.send(s+'\n')

	def received(self):
		ready = select.select([self.s], [], [], 5)
		if not ready[0]:
			self.s.close()
		else:
			try:
				s = self.s.recv(25)
			except socket.error:
				self.s.close()
			print ('Recv: {}'.format(s))

	def fire(self):
		self.send()
		self.received()

	def run(self):
		fires = [self.fire() for i in range(10000)]
		i = iter(fires)
		while True:
			try:
				next(i)
			except StopIteration: break


Kboom().run()
