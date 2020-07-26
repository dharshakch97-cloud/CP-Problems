# sameChars(s1, s2) [20 pts]
# Write the function sameChars(s1, s2) that takes two strings and returns True if the two strings are composed of 
# the same characters (though perhaps in different numbers and in different orders) -- that is, if every character 
# that is in the first string, is in the second, and vice versa -- and False otherwise. This test is 
# case-sensitive, so "ABC" and "abc" do not contain the same characters. The function returns False if either 
# parameter is not a string, but returns True if both strings are empty (why?).

def samechars(s1, s2):
	# Your code goes here
	if type(s1) == int or type(s2) == int:
		return False
	set1 = set()
	set2 = set()
	for i in s1:
		set1.add(i)
	for j in s2:
		set2.add(j)

	if len(set1) == len(set2):
		return True
	return False
	# print(set1)
	# print(set2)

print(samechars("abcabcabc", "cba"))
print(samechars("abcabcabc", "cbad"))
print(samechars("abcabcabc", "cBa"))
print(samechars(42,"The other parameter is not a string"))
print(samechars("", "a"))
