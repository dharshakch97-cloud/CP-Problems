# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 

def helper(n, k, d):
	l = list()
	while (n > 0):
		l.append(str(n%10))
		n = n//10
	if k >= len(l):
		l.append(str(d))
	else:
		l[k] = str(d)
	l.reverse()
	ans = "".join(l)
	return ans

def fun_set_kth_digit(n, k, d):
	if n < 0:
		n = abs(n)
		ans = helper(n, k, d)
		print(ans)
		ans = "-" + ans
		return int(ans)
	else:
		return int(helper(n, k, d))

print(fun_set_kth_digit(468, 0, 1))
print(fun_set_kth_digit(468, 1, 1))
print(fun_set_kth_digit(468, 2, 1))
print(fun_set_kth_digit(468, 3, 1))
print(fun_set_kth_digit(-468, 3, 1))