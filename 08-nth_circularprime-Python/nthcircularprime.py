# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

def isprime(n):
	if n > 1:
		for i in range(2, n):
			if n%i == 0:
				return False
		return True

def isCircularprime(n):
	i = 0
	count = 0
	if n < 10:
		if isprime(n):
			return True
		return False
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
	c = 2
	i = 3
	if n == 1:
		return 2
	while True:
		if isCircularprime(i):
			if c == n:
				return i
		i += 1
		c += 1

# isCircularprime(197)
print(nthcircularprime(1))
print(nthcircularprime(2))
print(nthcircularprime(3))
print(nthcircularprime(4))
print(nthcircularprime(5))
print(nthcircularprime(6))
print(nthcircularprime(7))
print(nthcircularprime(8))
print(nthcircularprime(9))
print(nthcircularprime(10))