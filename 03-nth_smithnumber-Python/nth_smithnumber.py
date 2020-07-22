# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

def factors(num):
    factors = []
    f = 2
    if num == 1:
        factors.append(1)
    else:
        while 1:
            if num%f == 0:
                factors.append(f)
                num //= f
                if num == 1:
                    return factors
            else:
                f += 1
    return factors

def sumdigits(n):
    s = 0
    while n > 0:
        r = n%10
        s += r
        n -= r
        n //= 10
    return s

def addlist(l):
    s = 0
    for i in range(len(l)):
        s += sumdigits(l[i])
    return s

def listsmith():
    for i in range(4, 500):
        f = factors(i)
        if len(f) > 1:
            if sumdigits(i) == addlist(f):
                print("{0} ".format(i))

def fun_nth_smithnumber(n):
    if n == 0:
        return 4
    count = 1
    # for i in range(5, 500):
    i = 5
    while True:
        f = factors(i)
        if len(f) > 1:
            if sumdigits(i) == addlist(f):
                if count == n:
                    return i
                count += 1
        i += 1
    # return 1

print(fun_nth_smithnumber(0))
print(fun_nth_smithnumber(1))
print(fun_nth_smithnumber(2))
print(fun_nth_smithnumber(5))
print(fun_nth_smithnumber(10))
print(fun_nth_smithnumber(15))
print(fun_nth_smithnumber(17))
print(fun_nth_smithnumber(19))