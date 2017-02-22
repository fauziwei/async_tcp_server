# fauziwei@yahoo.com

class Friend:
	__slots__ = ('lst')

	def __init__(self, lst):
		self.lst = lst

	def is_their_name(self):
		i = 0
		while i < len(self.lst):
			import time
			time.sleep(1)
			yield self.lst[i]
			i += 1

lst = ['fauzi', 'jiayou', 'xiaowan']
friend = Friend(lst)
name = friend.is_their_name()

say = lambda s: s*3

print say('Hello ')	;	print name.next()	;	print ' '
print say('Nihao ')	;	print name.next() ;	print ' '
print say('Nohao ')	;	print name.next() ;	print ' '

# while True:
# 	try:
# 		print name.next()
# 	except (StopIteration, \
# 		ValueError, \
# 		EnvironmentError) as err:
# 		break
