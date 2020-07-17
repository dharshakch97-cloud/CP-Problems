# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n 
# and returns the nth palindromic Prime, which is a palidrome number such that 
# it is also a prime. For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2


def isprime(n):
	for i in range(2, n):
		if n%i == 0:
			return False
	else:
		return True

def fun_nth_palindromic_prime(n):
	if n == 0:
		return 2
	
	count = 0
	i = 3

	while count != n:
		if str(i) == str(x)[::-1]:
			if isprime(i):
				count += 1
			if count == n:
				return i
		i += 1
		
	return False