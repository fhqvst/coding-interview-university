import math

def merge_sort(S):
	n = len(S)
	logn = math.ceil(math.log(n,2))
	src, dest = S, [None] * n
	for i in (2**k for k in range(logn)):
		for j in range(0, n, 2*i):
			merge(src, dest, j, i)
		src, dest = dest, src # edit the source for the next run
	if S is not src:
		S[0:n] = src[0:n]
	
# Merge src[start:start+inc] and src[start+inc:start+2*inc] into result
# Essentially merging two consecutive lists of length "inc" into result
def merge(src, result, start, inc):
	end1 = start + inc
	end2 = min(start+2*inc, len(src)) # take care of odd-length arrays
	x, y, z = start, start + inc, start
	while x < end1 and y < end2:
		if src[x] < src[y]:
			result[z] = src[x]; x += 1
		else:
			result[z] = src[y]; y += 1
		z += 1
	if x < end1: # copy remained of run 1 to output
		result[z:end2] = src[x:end1]
	elif y < end2:
		result[z:end2] = src[y:end2]

A = [3,2,1,31,51,25,-302,17,5]
merge_sort(A)
print(A)
