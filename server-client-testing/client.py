import sys
import select
import socket

m = 'Hello Im client\n'

host, port1, port2 = 'localhost', 1515, 1516
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port1))
print ('Send: {}'.format(m))
s.send(m)
recv = s.recv(25)
print ('Recv: {}'.format(recv))
s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port2))
print ('Send: {}'.format(m))
s.send(m)
recv = s.recv(25)
print ('Recv: {}'.format(recv))
s.close()