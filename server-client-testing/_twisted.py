# Twisted
import time
from twisted.internet import reactor, protocol, threads
from twisted.protocols.basic import LineOnlyReceiver

dtime = list()

class Protocol(LineOnlyReceiver):
	delimiter = '\n'

	def connectionLost(self, r):
		print ( 'lost connection.')
		self.transport.loseConnection()
		f = open('twisted.txt', 'w')
		for t in dtime:
			f.write('{0:.6f} '.format(t))
		f.close()

	def lineReceived(self, s):
		self.dt = time.time()
		print ('Recv: {}'.format(s))

		d = threads.deferToThread(Protocol.longPolling, s)
		d.addCallback(lambda s: self.sendStream(s))

	def sendStream(self, s):
		print ( 'Send: {}'.format(s.replace('client', 'server')))
		self.transport.write(s.replace('client', 'server'))
		stop = time.time() - self.dt
		dtime.append(stop)

	@staticmethod
	def longPolling(s):
		return s

class Factory(protocol.Factory):
	def buildProtocol(self, addr):
		return Protocol()

host, port = 'localhost', 1515
reactor.listenTCP(port, Factory())
reactor.run()