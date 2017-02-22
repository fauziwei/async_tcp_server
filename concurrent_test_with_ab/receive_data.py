import StringIO
import socket
from logging import warning as WARNING
from tornado.ioloop import IOLoop

def read_request(sock):
	buffer = StringIO.StringIO()
	while True:
		data = sock.recv(2048)
		if not data:
			break
		else:
			buffer.write(data)

	return buffer.getvalue()

def send_result(sock, data):
	if not sock:
		WARNING('ERROR: Socket None')
		return
	sock.send(data)
	#WARNING('Response was sent by worker.')
	sock.shutdown(socket.SHUT_WR)
	sock.close()

def sequential(port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('0.0.0.0', port))
	s.listen(500)
	sock_client, addr = s.accept()
	request = read_request(sock_client)
	#send_result(sock_client, "From worker: "+request)

if __name__ == '__main__':
	#while True:
	#	sequential(8001)
	sequential(8000)
	IOLoop.instance().start()
