# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
	if n == 0:
		return s
	if n > len(s):
		d = n - len(s)
		# lfirst = s[0:n]
		# lsecond = s[n:]
		return s[0:d] + s[d:]
	elif n < 0:
		return s[len(s)-abs(n):] + s[0:len(s)-abs(n)]
	else:
		return s[0:n] + s[n:]
	# print(lsecond + lfirst)
	# print(rsecond + rfirst)

print(fun_rotatestrings('abcd', 1))
print(fun_rotatestrings('ac323', 8))
print(fun_rotatestrings('abcd', 3))
# print(fun_rotatestrings('abcd', -6))