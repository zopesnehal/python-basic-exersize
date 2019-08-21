class Account:
	def __init__(self, value, value1):
		self.value = value
		self.value1 = value1

	def get_owner(self):
		return self.value + self.value1

acct = Account(2, 8)

print acct.get_owner()


acct1 = Account(4, 6)

print acct1.get_owner()