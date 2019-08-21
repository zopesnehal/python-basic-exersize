class Simple():
	def __init__(self,value):
		self.value = value

	def add_to_value(self,amount):

		self.value = self.value + amount
		print('we just added {} to your value'.format (amount))

myobj = Simple(300)
print(myobj.value)
myobj.add_to_value(100)
print(myobj.value)

