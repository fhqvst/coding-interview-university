def permutations(S):
	stack = []
	for i in range(len(S)):
		stack.append(S[0:len(S) - i)
	perms = []
	while (len(stack) > 0):
		items = stack.pop()
		if (len(perms) == 0):
			perms = [ items ]
		else:
			perms = [
