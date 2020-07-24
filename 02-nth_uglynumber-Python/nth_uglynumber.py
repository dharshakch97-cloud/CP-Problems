# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number. 
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.


def fun_nth_uglynumber(n):
    ugly = [0] * (n+1)
    ugly[0] = 1
    i = j = k = 0

    next2 = 2
    next3 = 3
    next5 = 5

    for m in range(1, n+1):
        ugly[m] = min(next2, next3, next5)
        if ugly[m] == next2:
            i += 1
            next2 = ugly[i]*2
        if ugly[m] == next3:
            j += 1
            next3 = ugly[j]*3
        if ugly[m] == next5:
            k += 1
            next5 = ugly[k]*5
    return ugly[-1]

print(fun_nth_uglynumber(0))
print(fun_nth_uglynumber(1))
print(fun_nth_uglynumber(2))
print(fun_nth_uglynumber(5))
print(fun_nth_uglynumber(10))
print(fun_nth_uglynumber(25))
print(fun_nth_uglynumber(50))
print(fun_nth_uglynumber(100))