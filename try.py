try:
	f = open('testfile','W')
	f.write("write a test line")
except: 
	print("there was a type error")

finally:
	print("i allways run")
