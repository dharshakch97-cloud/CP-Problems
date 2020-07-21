# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    res = [[sum(a * b for a, b in zip(i, j)) 
            for j in zip(*m2)] for i in m1]
    return res

print(fun_matrixmultiply([[12, 7, 3], [4, 5, 6], [7, 8, 9]], 
    [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]))




