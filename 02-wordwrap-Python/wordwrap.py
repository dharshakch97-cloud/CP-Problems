# Write the function wordWrap(text, width) that takes a string of text (containing only lowercase letters
#  or spaces) and a positive integer width, and returns a possibly-multiline string that matches the 
# original string, only with line wrapping at the given width. So wordWrap("abc", 3) just returns "abc", 
# but wordWrap("abc",2) returns a 2-line string, with "ab" on the first line and "c" on the second line. 
# After you complete word wrapping in this way, only then: All spaces at the start and end of each 
# resulting line should be removed, and then all remaining spaces should be converted to dashes ("-"), 
# so they can be easily seen in the resulting string. Here are some test cases for you:
# assert(wordWrap("  abcdefghij", 4)  ==  """\
# abcd
# efgh
# ij""")

# assert(wordWrap(" a b c de fgh ",  4)  ==  """\
# a-b-
# c-de
# -fgh""")

def fun_wordwrap(s, n):
	s = s.lstrip().rstrip().replace(" ", "-")
	# print(s)
	st = len(s)//n
	if len(s)%n > 0:
		st += 1

	s1 = str()
	for i in range(st):
		s1 += s[i*n: n*(i+1)]
		if i != st - 1:
			s1 += "\n"
	return s1 
print(fun_wordwrap(" a b c de fgh ",  4))
print(fun_wordwrap("  abcdefghij", 4))
 