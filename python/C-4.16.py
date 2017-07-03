def reverse(word):
	return word[0] if len(word) == 1 else word[-1] + reverse(word[:-1])

assert reverse('pots&pans') == 'snap&stop'
