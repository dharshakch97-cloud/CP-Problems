# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	d = dict()
	for i in str(n):
		if i in d:
			d[i] += 1
		else:
			d[i] = 0

	r = max(d.values())
	print(r)

print(mostfrequentdigit(26011))
