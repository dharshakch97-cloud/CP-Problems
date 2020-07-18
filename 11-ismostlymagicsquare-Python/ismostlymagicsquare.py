# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.

def ismostlymagicsquare(a):
	# Your code goes here
	res = [0]*((len(a)*2)+2)
	for i in range(len(a)):
		for j in range(len(a[i])):
			res[j + len(a[0])] += a[i][j]
		for k in range(len(a[i])):
			res[i] += a[i][k]
			if i == k:
				res[len(a)*2] += a[i][k]
			if len(a[i])-1-i == k:
				res[len(a)*2+1] += a[i][k]

	r = set(res)
	if len(r) == 1:
		return True
	return False

print(ismostlymagicsquare([[2, 7, 6], [9, 5, 1], [4, 3, 8]]))
print(ismostlymagicsquare([[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12],[4, 15, 14, 1]]))
print(ismostlymagicsquare([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))