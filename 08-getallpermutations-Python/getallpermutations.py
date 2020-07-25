# getallPermutations(str) [20 pts]
# Write an efficient program to print all permutations of a given String. For example, if given input is "abc" then 
# your program should print all 6 permutations e.g. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

def getpermutation(s):
	l = []
	for i in range(len(s)):
		p = s[i]
		rem = s[:i] + s[i+1:]
		for q in getpermutation(rem):
			l.append([p] + q)
	return l

def getallpermutations(x):
	# Your code goes here
	s = list(x)
	print(s)
	return getpermutation(s)

print(getallpermutations("ABC"))