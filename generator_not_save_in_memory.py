# fauziwei@yahoo.com

# LIST = save data in memory
# GENERATOR = only once and gone

friends = ['xiaowan', 'xiaosu', 'wuqiang']

for i in range(3):
	for friend in friends:
		print friend

friends = (x*x for x in range(3))

for friends in friends:
	print friends
# for friends in friends: # HERE cannot be iterated anymore
# 	print friends
