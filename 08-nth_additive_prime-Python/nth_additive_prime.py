# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2


def isprime(n):
	for i in range(2, n//2):
		if  n%i == 0: return True
	return False

def fun_nth_additive_prime(n):
	nums = list(map(int, str(n)))
	s = sum(nums)
	if isprime(s):
		return True
	return False