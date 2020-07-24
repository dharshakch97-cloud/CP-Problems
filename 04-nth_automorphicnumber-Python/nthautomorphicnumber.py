# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

def isautomorphic(n):
	sq = n**2
	last = sq%pow(10, len(str(n)))
	# print(last)
	if last == n:
		return True
	return False
	
def nthautomorphicnumbers(n):
	# Your code goes here
	i = 0
	count = 0
	while True:
		if isautomorphic(i):
			count += 1
			if count == n:
				return i
		i += 1

print(isautomorphic(0))
print(nthautomorphicnumbers(1))
print(nthautomorphicnumbers(2))
print(nthautomorphicnumbers(3))
print(nthautomorphicnumbers(14))
print(nthautomorphicnumbers(15))
print(nthautomorphicnumbers(16))