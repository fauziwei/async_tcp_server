import matplotlib.pyplot as plt

f1 = open('twisted.txt')
f2 = open('tornado.txt')

lines = (line.split(' ') for line in f1)
lines1 = [line for line in lines][0]
lines1 = map(float, lines1[0:-1]) # last is ''

lines = (line.split(' ') for line in f2)
lines2 = [line for line in lines][0]
lines2 = map(float, lines2[0:-1]) # last is ''

f1.close()
f2.close()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('step')
ax.set_ylabel('time process')
ax.grid(True)
p1 = ax.plot(lines1)
p2 = ax.plot(lines2)

ax.legend((p1[0], p2[0]), ('twisted', 'tornado'), loc='best', fancybox=True, framealpha=0.5)
plt.show()