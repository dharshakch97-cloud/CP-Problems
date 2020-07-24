# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….

def reverse(n):
	r = 0
	while n > 0:
		rem = n%10
		r = (r*10) + rem
		n = n//10
	return r

def islycherel(n):
	for i in range(20):
		n = n + reverse(n)
		if n == reverse(n):
			return False
	return True

def nthlychrelnumbers(n):
	# your code goes here
	count = 0
	i = 196
	while True:
		if islycherel(i):
			count += 1
			if count == n:
				return i
		i += 1

print(nthlychrelnumbers(0))
# print(nthlychrelnumbers(1))
# print(nthlychrelnumbers(2))