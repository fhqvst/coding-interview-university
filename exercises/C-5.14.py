from random import randrange

def shuffle(x):
	for i in range(len(x)):
		k = randrange(0, len(x) - 1)
		y = x[k]
		x[k] = x[i]
		x[i] = y

x = [1,2,3,4,5,6,7,8]
shuffle(x)
print(x)
