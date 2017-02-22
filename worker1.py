# fauziwei@yahoo.com

from tornado.tcpserver import TCPServer
from tornado.ioloop import IOLoop

class Connection(object):
	_conn = set()

	def __init__(self, stream, address):
		Connection._conn.add(self)
		self._stream = stream
		self._address = address
		self._stream.set_close_callback(self.on_close)
		self.read_message()
		print address, "A new user has entered."

	def on_close(self):
		print self._address, "A user has left"
		Connection._conn.remove(self)

	def read_message(self):
		self._stream.read_until('\n', self.broadcast_messages)

	def broadcast_messages(self, data):
		print self._address, "User said:", data[:-1]
		for con in Connection._conn:
			con.send_message(data)
		self.read_message()

	def send_message(self, data):
		self._stream.write(data)

class ChatServer(TCPServer):
	def handle_stream(self, stream, address):
		Connection(stream, address)

if __name__ == '__main__':
	server = ChatServer()
	server.listen(8001)
	IOLoop.instance().start()
