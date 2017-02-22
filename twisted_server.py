# fauziwei@yahoo.com

import time
from twisted.internet import protocol, reactor, threads
from twisted.protocols.basic import LineReceiver

class Protocol(LineReceiver):
	_clients = set()
	def __init__(self):
		self.delimiter = '\n'

	# def connenctionMade(self):
	# 	pass

	def connectionLost(self, reason):
		print ('close connection')
		self.transport.loseConnection()
		Protocol._clients.discard(self)

	def lineReceived(self, data):
		print ('Received: {}'.format(repr(data)))
		d = threads.deferToThread(self.long_polling, data)
		d.addCallback(lambda s: self.send_stream(data))

	def send_stream(self, data):
		print ('Send: {}'.format(data))
		self.transport.write('{}'.format(repr(data)))

	def long_polling(self, data):
		return 'Hello Im server'

class Factory(protocol.Factory):
	def buildProtocol(self, addr):
		return Protocol()

reactor.listenTCP(1515, Factory())
reactor.run()