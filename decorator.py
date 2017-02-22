def massive_call(myfunc):
	def inner_func(*args, **kwargs):
		for i in range(100):
			myfunc(*args, **kwargs)
	return inner_func


@massive_call
def hello():
	print "hello"


hello()