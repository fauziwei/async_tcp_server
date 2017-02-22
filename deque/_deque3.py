import collections
import threading
import time

candle = collections.deque(xrange(5))

i = iter(candle)
while True:
	try:
		print i.next()
	except StopIteration:
		break