# leastFrequentLetters(s) [20 pts]
# Write the function leastFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated 
# the same), returns a lowercase string containing the least-frequent alphabetic letters that occur in s, each 
# included only once in the result and then in alphabetic order. So:
# leastFrequentLetters("aDq efQ? FB'daf!!!") 
# returns "be". Note that digits, punctuation, and whitespace are not letters! Also note that seeing as we have not 
# yet covered lists, sets, maps, or efficiency, you are not expected to write the most efficient solution. Finally, 
# if s does not contain any alphabetic characters, the result should be the empty string ("")

def leastfrequentletters(s):
	# Your code goes here
	s = s.lower()
	lf = dict()
	for i in s:
		ch = ord(i)
		if ch > 97 and ch < 122:
			if i not in lf:
				lf[i] = 1
			else:
				lf[i] += 1
	print(lf)
	r = ""
	for i in lf.keys():
		if lf[i] == 1:
			r += str(i)
	print(r)
	return r

print(leastfrequentletters("aDq efQ? FB'daf!!!"))
# print(leastfrequentletters("?'!!"))
# print(leastfrequentletters("abc def! GFE'cag!!!"))