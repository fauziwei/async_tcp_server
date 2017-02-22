def bigboom(i):
	print  "I'm a boom: %s" % i
	import time
	time.sleep(0.1)

booms = [ bigboom(i) for i in range(1000) ]

i = iter(booms)
while True:
	try:
		next(i)
	except StopIteration:
		break