def async(lst):
	i = 0
	while True:
		yield lst[i]
		i += 1


try:
	for i in async(xrange(1, 100, 1)):
		print i
except:
	pass