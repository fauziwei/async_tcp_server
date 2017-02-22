import collections

data = [1,2,3,4]
d = collections.deque(data)
# print d.popleft()
# print d
d.appendleft(10)
# print d
# print len(d)
# print d[0]

# i = iter(d)
# k = 0
# while True:
# 	try:
# 		n = i.next()
# 		d[2] = 10
# 		k += 1
# 	except StopIteration:
# 		break

# print d

# print d.popleft()
# print d.popleft()
# print d.popleft()
# print d.popleft()
# print d.popleft()

while True:
	try:
		i = d.popleft()
		print i
		break
	except IndexError:
		break




# new_data = collections.deque()
# new_data.append('10')
# new_data.append('11')
# print 'new_data: %s' % new_data


# def get(dd):
# 	dd.appendleft(90)
# 	return dd

# c = get(d)
# print 'c:', c

# ddd = collections.deque(['h', 'b'])
# print 'ddd:', ddd

# c.extend(ddd)
# print 'c:', c

# ddd = c
# print 'ddd:', ddd