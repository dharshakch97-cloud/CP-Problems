# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	ch = dict()
	for i in s:
		if i in ch:
			ch[i] += 1
		else:
			ch[i] = 1

	occ = list(ch.values()).sort()
	print(occ)
	return ch

print(fun_kth_occurrences("helllo woorld", 2))
