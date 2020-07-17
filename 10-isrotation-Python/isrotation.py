# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotation(x, y):
	# Your code goes here
	str1 = str(x)
	str2 = str(y)

	s = str()
	str3 = str2[:1:]
	for i in str1:
		if str3 != i:
			s += i
		if str3 == i:
			break
	
	for i in range(len(str1)):
		if str1[i] == str3:
			str4 = str1[i::]

	res = str4 + s
	if res == str2:
		return True
	else:
		return False