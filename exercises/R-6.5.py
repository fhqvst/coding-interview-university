def reversed(S):
	stack = []
	for i in S:
		stack.append(i)
	return [ stack.pop() for i in S ]

s = [1,2,3,4,5]
t = reversed(s)

assert t == [5,4,3,2,1]
