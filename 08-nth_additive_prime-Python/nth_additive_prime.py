# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2


def isprime(n):
	for i in range(2, n):
		if  n%i == 0: 
			return False
	else:
		return True

def fun_nth_additive_prime(n):
	if n == 0:
		return 2
	
	count = 0
	i = 3

	while count != n:
		if isprime(i):
			# s = sum(list(map(int, str(n))))
			s = 0
			temp = i
			while temp != 0:
				t = temp%10
				s += t
				temp = temp//10
			if isprime(s):
				count += 1
			if count == n:
				return i
		i += 1
	return False

print(fun_nth_additive_prime(0))
print(fun_nth_additive_prime(1))
print(fun_nth_additive_prime(5))
print(fun_nth_additive_prime(7))
print(fun_nth_additive_prime(20))
print(fun_nth_additive_prime(25))