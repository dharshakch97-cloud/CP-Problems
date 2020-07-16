# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.



def fun_interleave(s1,s2):
	str = ""
	if len(s1) == len(s2):
		for i in range(len(s1)):
			str += s1[i] + s2[i]
		return str
	elif len(s1) > len(s2):
		for i in range(len(s2)):
			str += s2[i] + s1[i]
		str += s1[len(s2):len(s1):1]
		return str
	elif len(s2) > len(s1):
		for i in range(len(s1)):
			str += s2[i] + s1[i]
		str += s2[len(s1):len(s2):1]
		return str
	return ""
	
print(fun_interleave("pto", "yhn"))