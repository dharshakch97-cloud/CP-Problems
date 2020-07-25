# getallPermutations(str) [20 pts]
# Write an efficient program to print all permutations of a given String. For example, if given input is "abc" then 
# your program should print all 6 permutations e.g. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

def getpermutation(a, i, j):
	if i == j:
		return a
	else:
		for p in xrange(i, j+1):
			a[i], a[p] = a[p], a[i]
			getpermutation(a, i+1, j)
			a[i], a[p] = a[p], a[i]

def getallpermutations(x):
	# Your code goes here
	s = list(x)
	return getpermutation(s, 0, len(x)-1)

getallpermutations("ABC")