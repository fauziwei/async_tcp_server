import socket, traceback, os, sys
from threading import Thread, currentThread
import StringIO

def read_request(sock):
	print "New child", currentThread().getName()
	print "Got connection from", sock.getpeername()
	buffer = StringIO.StringIO()
	while True:
		data = sock.recv(2048)
		if not data:
			break
		buffer.write(data)
		print '%s\n' % buffer.getvalue()
	send_result(sock, buffer.getvalue())

def send_result(sock, data):
	sock.sendall("worker send: %s" % data)
	#sock.send("worker send: %s" % data)
	#sock.shutdown(socket.SHUT_WR)
	sock.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8001))
s.listen(1)
clientsock, addr = s.accept()

#while True:
#	try:
#		clientsock, addr = s.accept()
#	except KeyboardInterrupt:
#		raise
#	except:
#		traceback.print_exc()
#		continue


t = Thread(target = read_request, args= [clientsock])
t.setDaemon(1)
t.start()
t.join()