from operator import xor

# Does not work. Tried at least!

ls = [1,2,7,2,7,8,9,12]
def getNext():
	# Clean duplicates
	dupes = {}
	lss = []
	for i in ls:
		if (dupes.get(i, 0) == 0):
			lss.append(i)
			dupes[i] = 1

	# XOR all numbers to get a new number
	temp = None
	for i in lss:
		if (temp == None):
			temp = i
		else:
			temp = xor(temp, i)
	return temp

print(getNext())
