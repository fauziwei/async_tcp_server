# fauziwei@yahoo.com

class Bank:
	crisis = False
	def create_atm(self):
		while not self.crisis:
			yield '$100'

hsbc = Bank()
corner_street = hsbc.create_atm()
print corner_street.next()
# print corner_street.next()

# print [corner_street.next() for cash in range(5)]

# hsbc.crisis = True
# print corner_street.next()