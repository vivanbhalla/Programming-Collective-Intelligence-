# Script to implement an alogirthm to determine if a string has unique characters or not

def BinarySearch(input,target):
	first=0
	last=len(input)-1

	# Check for input length 
	if len(input) == 0:
		return False
	elif len(input) == 1:
		if [input[0] == target]:
			return True
		else:
			return False

	



