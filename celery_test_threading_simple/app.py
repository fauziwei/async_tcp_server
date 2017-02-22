import os.path
import sys
import threading

basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(basedir)

import friend


def threadcode(my):
	a = 5
	b = 10
	if my == 'one': # slowest
		task = friend.spread_another_cpu.apply_async(args=(a, b), timeout=60)
		count = task.get()
		print('one: {}'.format(count))
	elif my == 'two': # middle
		task = friend.hit.apply_async(args=(a, b), timeout=50)
		count = task.get()
		print('two: {}'.format(count))
	else: # fast
		task = friend.hit.delay(a, b)
		count = task.get()
		print('three: {}'.format(count))


tlist = []
for i in ['one', 'two', 'three']:
	t = threading.Thread(target=threadcode, args=(i,))
	t.start()
	tlist.append(t)

for t in tlist:
	t.join()



import gevent
import gevent.monkey
gevent.monkey.patch_all()
threads = []
for i in ['one', 'two', 'three']:
	threads.append(gevent.spawn(threadcode, i))
gevent.joinall(threads)