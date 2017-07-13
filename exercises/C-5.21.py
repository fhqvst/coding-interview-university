from time import time

# String concatenation
start = time()
string = ''
for i in range(1000000):
	string = string + 'a'
end = time()
ex1 = end - start

# Appending to a temporary list and joining
start = time()
string = []
for i in range(1000000):
	string.append('a')
''.join(string)
end = time()
ex2 = end - start

# List comprehension with join
start = time()
string = [ 'a' for i in range(1000000) ]
''.join(string)
end = time()
ex3 = end - start

# Generator comprehension with join
start = time()
string = ( 'a' for i in range(1000000) )
''.join(string)
end = time()
ex4 = end - start

print(ex1)
print(ex2)
print(ex3)
print(ex4)
