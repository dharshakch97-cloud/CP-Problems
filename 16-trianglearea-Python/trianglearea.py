# trianglearea(s1, s2, s3)[5pts]
# Write the function trianglearea(s1, s2, s3) that takes 3 floats/ints and returns the area of the
# triangle that has those lengths of its side. If no such triangle exists, return 0. Hint: you
# will probably wish to use Heron's Formula.

import math

def isLegaltriangle(s1, s2, s3):
	if s1 <= 0 or s2 <= 0 or s3 <= 0:
		return False
	max_side = max(s1, s2, s3)
	if (max_side == s1 and s2 + s3 > s1):
		return True
	elif (max_side == s2 and s1 + s3 > s2):
		return True
	elif (max_side == s3 and s1 + s2 > s3):
		return True
	else:
		return False

def trianglearea(s1, s2, s3):
	# your code goes here
	if isLegaltriangle(s1, s2, s3):
		s = (s1+s2+s3)/2
		return math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
	else:
		return 0
