# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def istidy(n):
    n = str(n)
    s = sorted(list(map(int, n)))
    r = ""
    for i in s:
        r += str(i)
    return n == r
    
def fun_nth_tidynumber(n):
    count = -1
    i = 1
    while True:
        if istidy(i):
            count += 1
            if count == n:
                return i
        i += 1
    # return 0

print(istidy(1))
# print(istidy(34567))
print(fun_nth_tidynumber(0))
print(fun_nth_tidynumber(1))
print(fun_nth_tidynumber(5))
print(fun_nth_tidynumber(15))
print(fun_nth_tidynumber(35))
print(fun_nth_tidynumber(50))
print(fun_nth_tidynumber(100))
print(fun_nth_tidynumber(250))
print(fun_nth_tidynumber(500))