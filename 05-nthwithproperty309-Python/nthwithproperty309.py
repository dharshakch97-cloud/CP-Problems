# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def prop309(n):
	s = str(n**5)
	s = set(list(map(int, s)))
	if len(s) == 10:
		return True
	return False

def nthwithproperty309(n):
	# Your code goes here
	count = -1
	i = 309
	while True:
		if prop309(i):
			count += 1
			if count == n:
				return i
		i += 1

print(nthwithproperty309(0))