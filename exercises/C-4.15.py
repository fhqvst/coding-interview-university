def find_subsets(nums):
	if (len(nums) == 0):
		return [[]]
	x = nums.pop(0)
	subsets = find_subsets(nums)
	combined = [ [x] + s for s in subsets ]
	return combined + subsets   


subsets = find_subsets([1,2,3])
frozen = set(map(frozenset, subsets))

assert frozen == set(map(frozenset, [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]))
