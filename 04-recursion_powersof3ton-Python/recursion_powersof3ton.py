# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

res = list()
def powers3(num):
	if num > 1 and num % 3 == 0:
		return powers3(num//3)
	elif num == 1:
		return True
	return False

def recursion_powersof3ton(n):
	# Your code goes here
	n = int(n)
	if n > 0:
		global res
		if powers3(n):
			res.append(n)
		return recursion_powersof3ton(n-1)
	elif len(res) > 0:
		r = sorted(res)
		res = list()
		return r
	return None
print(recursion_powersof3ton(10.5))