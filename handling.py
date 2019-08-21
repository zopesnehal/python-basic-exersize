def add(n1,n2):
	print n1+n2

add(10,20)

number2 = input("please provide a number2:")
number1 = input("please provide a number:")
add(number1,number2)
print("something happend!")

try:
# want to attempt this code 
# may have an error
	result = 10 + 10
	print("adad went well")
	print(result)
except:
	print("hey its looks like you are not adding correctly!")
else:
	print("add went well")
	