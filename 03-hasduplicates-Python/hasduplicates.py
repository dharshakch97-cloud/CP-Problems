# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
	# Your code goes here
	L_len = sum(len(row) for row in L)
	s = set()
	# print(L_len)
	for i in L:
		for j in i:
			s.add(j)

	if len(s) != L_len:
		return True
	return False

print(hasduplicates([[2, 7, 9], [9, 5, 1], [4, 3, 8]]))
print(hasduplicates([[2, 7, 6], [9, 5, 1], [4, 3, 8]]))