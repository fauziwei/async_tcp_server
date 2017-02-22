import collections

def foo():
	for i in range(5):
		print 'Im foo: %s' % i
		yield

def bar():
	for i in range(5):
		print 'Im bar: %s' % i
		yield

def spam():
	for i in range(5):
		print 'Im spam: %s' % i
		yield

tasks = collections.deque()
tasks.append(foo())
tasks.append(bar())
tasks.append(spam())

while tasks:
	task = tasks.popleft()
	try:
		next(task)
		tasks.append(task)
	except StopIteration:
		# task is done
		pass