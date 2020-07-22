# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



import math
def kaprekar(n):
    if n == 1:
        return 1
    sq = n*n
    count = 0
    while sq != 0:
        count += 1
        sq //= 10
    
    sq = n*n
    for i in range(1, count):
        div = int(math.pow(10, i))
        if div == n:
            continue
        s = int(sq/div) + int(sq%div)
        if s == n:
            return True
    return False

def fun_nearestkaprekarnumber(n):
    ls = list()
    ls.append(n)
    while True:
        if kaprekar(n):
            return n
        if not kaprekar(n-1):
            j = (n-1)-1
            while True:
                if kaprekar(j):
                    ls.append(j)
                    break
                j -= 1
        if not kaprekar(n+1):
            i = (n+1)+1
            while True:
                if kaprekar(i):
                    ls.append(i)
                    break
                i += 1
        # print(ls)
        a = ls[0] - ls[1]
        b = ls[2] - ls[0]
        if a <= b:
            return ls[1]
        return ls[2]
    # return kaprekar(45)

print(fun_nearestkaprekarnumber(49))
print(fun_nearestkaprekarnumber(51))
print(fun_nearestkaprekarnumber(50))
print(fun_nearestkaprekarnumber(102))
print(fun_nearestkaprekarnumber(765))
print(fun_nearestkaprekarnumber(3861))