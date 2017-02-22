import collections
import threading
import time

candle = collections.deque(xrange(5))

def burn(direction, nextSource):
	while True:
		try:
			next = nextSource()
		except IndexError:
			break
		else:
			print '{0:8s}: {1}'.format(direction, next)
			time.sleep(0.1)
	print '{0:8s} done'.format(direction)

left = threading.Thread(target=burn, args=('Left', candle.popleft))
right= threading.Thread(target=burn, args=('Right', candle.pop))

left.start()
right.start()

left.join()
right.join()