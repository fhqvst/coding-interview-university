from time import time

N = 10000

ls = [ 'a' for n in range(N) ]
ls.extend([ 'b' for n in range(N) ])
ls.extend([ 'c' for n in range(N) ])
for n in range(N):
	start = time()
	ls.remove('a')
	end = time()
	ex1 = end - start

ls = [ 'a' for n in range(N) ]
ls.extend([ 'b' for n in range(N) ])
ls.extend([ 'c' for n in range(N) ])
for n in range(N):
	start = time()
	ls.remove('b')
	end = time()
	ex2 = end - start

ls = [ 'a' for n in range(N) ]
ls.extend([ 'b' for n in range(N) ])
ls.extend([ 'c' for n in range(N) ])
for n in range(N):
	start = time()
	ls.remove('c')
	end = time()
	ex3 = end - start


print(ex1)
print(ex2)
print(ex3)
