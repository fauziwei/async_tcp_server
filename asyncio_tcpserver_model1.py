# fauziwei@yahoo.com

import asyncio

host, port = '127.0.0.1', 1515
print ( 'Host: {} , Port: {}'.format(host, port) )
loop = asyncio.get_event_loop()

class Simple(asyncio.Protocol):

	def connection_made(self, transport):
		self.transport = transport

	def data_received(self, s):
		s = s.decode('utf-8')
		print ( 'Recv: {}'.format(s) )
		# m = 'Hello Im server'
		# print ( 'Send: {}'.format(m) )
		# self.transport.write( m.encode('utf-8') )

	def connection_lost(self, s): pass

talk = loop.create_server(Simple, host, port)
loop.run_until_complete(talk)
try: loop.run_forever()
finally: loop.close()