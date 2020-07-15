# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	n = abs(digit)
	n = (n/(10**k))%10
	# n = n//1
	# n = n%10
	return int(n)

print(fun_get_kth_digit(789, 0))
print(fun_get_kth_digit(789, 1))