try:
	for i in [a,b,c]:
		print(i**2)
except:
	print("genral error!watch out1")

try:
	x = 5
	y = 0
	z = x/y
except:
	print("error!")
finally:
	print("All done")

def ask():
	while true:
		try:
			n = int(input("Enter a nnumber"))
		except:
			print("please try again! \n")
			continue
		else:
			break
	print("your number squaared is:")
	print(n**2)
ask()
enter a number10