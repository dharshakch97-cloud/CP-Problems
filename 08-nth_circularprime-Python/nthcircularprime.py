# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

def isprime(n):
	for i in range(2, n):
		if n%i == 0:
			return False
	return True

def isCircularprime(n):
	i = 0
	count = 0
	l = len(str(n))
	while i < l:
		r = n%10
		n = n//10
		n = int((r*(10**(l-1)) + n))
		# print(n)
		if isprime(n):
			count += 1
		i += 1
	if count == l:
		return True
	return False

def nthcircularprime(n):
	# Your code goes here
	c = 1
	i = 3
	if n == 1:
		return 2
	while True:
		if isCircularprime(i):
			c += 1
			if c == n:
				return i
		i += 1

# isCircularprime(197)
print(nthcircularprime(3))