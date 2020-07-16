# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
	# Your code goes here
	if len(a) == 1:
		return a[0]
	elif len(a) > 0:
		l = sorted(a)
		d = l[1] - l[0]
		for i in range(1, len(a) - 1):
			d1 = a[i + 1] - a[i]
			if d > d1:
				d = d1
		return d
	else:
		return -1

print(smallestdifference([3, -7, 0]))
print(smallestdifference([-59,-36,-13,1,-53,-92,-2,-96,-54,75]))