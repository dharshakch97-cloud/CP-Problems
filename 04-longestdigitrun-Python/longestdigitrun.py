# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).

def lookandsay(l):
	count = 1
	ls = list()
	for i in range(1, len(l)+1):
		if i < len(l) and l[i-1] == l[i]:
			count += 1
		else:
			ls.append((count, l[i-1]))
			count = 1
	return ls

def longestdigitrun(n):
	# Your code goes here
	l = list(map(int, str(abs(n))))
	ls = lookandsay(l)
	m = p = 0
	for i in ls:
		if i[0] > m:
			m = i[0]
			p = i[1]
		if i[0] == m and p > i[1]:
			p = i[1]
	return p

print(longestdigitrun(117773732))
print(longestdigitrun(-677886))
print(longestdigitrun(112233455567))
print(longestdigitrun(44332211))