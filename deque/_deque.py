import collections

d = collections.deque('abcdefg')
print 'Deque:', d
print 'Length:', len(d)
print 'Left end:', d[0]

d.remove('c')
print 'remove(c):', d

# support LIST operation