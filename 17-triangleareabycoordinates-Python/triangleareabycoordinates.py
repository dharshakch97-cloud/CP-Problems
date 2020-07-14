# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.

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

def distance(x1, y1, x2, y2):
	return math.sqrt((x2 - x1)**2 + ((y2 - y1)**2))

def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
	# your code goes here
	a = distance(x1, y1, x2, y2)
	b = distance(x2, y2, x3, y3)
	c = distance(x3, y3, x1, y1)
	return trianglearea(a, b, c)