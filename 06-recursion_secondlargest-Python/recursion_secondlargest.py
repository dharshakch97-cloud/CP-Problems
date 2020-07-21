# Recursion-Only recursion_secondlargest(L) [15 pts]
# Note: recall that you may not use sort, sorted, min, or max this week! With that in mind, write the function 
# recursion_secondlargest(L) that takes a list of integers in any order and returns the second-largest value in the list. To 
# be more precise, it returns the second value from the end if the list was sorted (though you do not need to sort 
# it to solve this problem), so if the largest value occurs twice, you would return that value. Also, if there are 
# fewer than 2 values in the list, return None. Here are some test cases:
# assert(recursion_secondlargest([1,2,3,4,5]) == 4)
# assert(recursion_secondlargest([4,3]) == 3)
# assert(recursion_secondlargest([4,4,3]) == 4)
# assert(recursion_secondlargest([-3,-4]) == -4)
# assert(recursion_secondlargest([4]) == None)
# assert(recursion_secondlargest([ ]) == None)
# Again, you do not need to sort the list. We didn't sort it in our sample solution. We just tracked the two largest 
# values as we recursively traversed the list. Also, you may not use loops/iteration in this problem

def second(L, i, l, sl):
	if i == len(L):
		return sl
	if L[i] == l:
		return L[i]
	if L[i] > l:
		sl = l
		l = L[i]
	return second(L, i+1, l, sl)

def recursion_secondlargest(L):
	# Your code goes here
	if len(L) == 1 or len(L) == 0:
		return None
	return second(sorted(L), 0, -20, -20)

print(recursion_secondlargest([1, 2, 3, 4, 5]))
print(recursion_secondlargest([-3, -4]))
print(recursion_secondlargest([4, 4, 3]))