# fauziwei@yahoo.com

import sys
import select
import socket

def call():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect(('127.0.0.1', 1515))
		s.setblocking(False)
	except socket.error:
		s.close()
		print ( 'Socket error')
		sys.exit()

	m = 'Hello, Im client'
	print ( 'Send: {}'.format(m) )
	s.send( m.encode('utf-8') )

	timeout = 15
	ready = select.select([s], [], [], timeout)
	try:
		if not ready[0]:
			s.close()
			print ( 'Recv > timeout {}'.format(timeout) )
		else:
			try:
				buffer = 128
				recv = s.recv(buffer)
			except socket.error:
				s.close()
				print ( 'Recv Failed' )
			print ( 'Recv: {}'.format(recv.decode('utf-8')) )
	except socket.error:
		s.close()
	finally:
		pass

calls = [call() for i in range(100000)]

# i = iter([call(), call()])
i = iter(calls)
while True:
	try:
		next(i)
	except StopIteration:
		break