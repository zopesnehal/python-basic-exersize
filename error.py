try:
	f = open('testfile', 'w')
	f.write("write a test line")
except:
	print('All other eception!')
finally:
	print("I always run")