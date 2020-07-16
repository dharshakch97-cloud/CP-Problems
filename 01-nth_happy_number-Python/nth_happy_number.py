# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)

def squares(n):
	sum = 0
	while n > 0:
		r = n % 10
		sum += r * r
		n = n // 10
	return sum

def ishappynumber(n):
	# your code goes here
	numList = list()
	if n == 1:
		return True
	elif n > 0:
		while True:
			n = squares(n)
			if n == 1:
				return True
			elif n in numList:
				return False
			else:
				numList.append(n)
	else:
		return False

def fun_nth_happy_number(n):
	count = 0
	if n > 0:
		while count != n:
			while True:
				i += 1
				if ishappynumber(i):
					break
			count += 1
		return i
	else:
		return 1
