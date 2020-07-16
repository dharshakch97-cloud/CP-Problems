# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().

'''
	s1 = helloworld123 s2 = hello s3 = 345
'''

def fun_replace(s1, s2, s3):
	str = s1.split(s2)
	print(str)
	if len(str[0]) == len(s1):
		return s1
	return s1

fun_replace("helloworld123", "hello", "345")
fun_replace("helloworld123", "123", "345")
fun_replace("helloworld123", "34567", "345")