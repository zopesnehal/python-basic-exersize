def ran_cheak(num,low,high):
	if num in range(low,high):
		print "%s is in the range" %str(num)
	else :
		print " the number is outside the range."
 
def ran_bool(num,low,high):
	return num in range(low,high)
ran_bool(3,1,10)