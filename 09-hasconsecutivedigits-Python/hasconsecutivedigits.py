# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	n = list(str(n))
	check = set(n)
	if len(n) != len(check):
		return True
	return False

print(hasconsecutivedigits(26011))
print(hasconsecutivedigits(24))