def palindrome(word):
	return True if len(word) < 2 else word[0] == word[-1] and palindrome(word[1:-1])

assert palindrome('racecar')
assert palindrome('rabbar')
assert not palindrome('derp')
