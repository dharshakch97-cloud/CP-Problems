# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0 
# and which remains prime when the leading (left) digit is successively removed. 
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime. 
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and 
# nthLeftTruncatablePrime(10) returns 53.



import math
def isprime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def lefttruncatebyone(n):
    if n < 10 and isprime(n):
        return True
    else:
        s = str(n)
        while len(s) != 0:
            if isprime(int(s)):
                s = s[1:]
            else:
                return False
        return True

def fun_nth_lefttruncatableprime(n):
    if n == 0:
        return 2
    c = 0                          #  3 -> 1, 5 -> 2, 7 -> 3, 13 -> 4, 17 
    i = 3
    while True:
        if lefttruncatebyone(i):
            c += 1
            if c == n:
                # print(i)
                return i
        i += 1
# print(lefttruncatebyone(35))
print(fun_nth_lefttruncatableprime(0))
print(fun_nth_lefttruncatableprime(1))
print(fun_nth_lefttruncatableprime(2))
print(fun_nth_lefttruncatableprime(3))
print(fun_nth_lefttruncatableprime(4))
print(fun_nth_lefttruncatableprime(5))