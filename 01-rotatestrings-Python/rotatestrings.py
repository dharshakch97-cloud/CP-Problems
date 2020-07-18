# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
	lfirst = s[0:n]
	lsecond = s[n:]
	rfirst = s[0:len(s)-n]
	rsecond = s[len(s)-n:]

	if n > 0:
		return lsecond + lfirst
	else:
		return rsecond + rfirst

print(fun_rotatestrings('abcd', 1))
print(fun_rotatestrings('ac323', 8))
