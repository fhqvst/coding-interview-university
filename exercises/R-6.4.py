def remove_all(S):
	if len(S) == 0:
		return
	S.pop()
	return remove_all(S)

s = [1,2,3,4,5]
remove_all(s)

assert s == []
