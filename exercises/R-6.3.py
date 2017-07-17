def transfer(S, T):
	while len(S) > 0:
		T.append(S.pop())

s = [1,2,3,4,5]
t = []
transfer(s, t)
assert t == [5,4,3,2,1]
