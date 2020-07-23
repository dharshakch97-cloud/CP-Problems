# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

def isprime(n):
	for i in range(2, n):
		if n%i == 0:
			return False
	return True

def ispowerful(n):
	i = 2
	c = n//2
	f = 0
	while c >= i:
		if isprime(i) and n%i == 0:
			f = 1
			if n%(i**2) != 0:
				return False
		i += 1
	if f == 0:
		return False
	return True

def nthpowerfulnumber(n):
	# Your code goes here
	if n == 0:
		return 1
	count = 0
	i = 2
	while count < n:
		if ispowerful(i):
			count += 1
		i += 1
	return i - 1

print(nthpowerfulnumber(4))
