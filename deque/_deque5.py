import collections

d = collections.deque(xrange(10))

d.rotate(2)
print d

d.rotate(-2)
print d