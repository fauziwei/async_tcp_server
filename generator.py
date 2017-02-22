# fauziwei@yahoo.com

def hit_me(lst):
	i = 0
	while i < 9999:
		yield i
		i += 1

for i in hit_me(range(1000)):
	print i