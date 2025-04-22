# binary solve equation
# xyan831

# import module
from math import sqrt, log

# 4^x + 6^x = 9^x
def check(x):
    lhs = 4**x + 6**x
    rhs = 9**x
    return lhs - rhs

# find x
def binary_solve(left, right):
    mid = (left+right)/2
    result = check(mid)
    if abs(result) <= 0.0001:
        return mid
    else:
        while abs(result) > 0.0001:
            if result > 0:
                left = mid
                mid = (left+right)/2
                result = check(mid)
                if abs(result) <= 0.0001:
                    return mid
            elif result < 0:
                right = mid
                mid = (left+right)/2
                result = check(mid)
                if abs(result) <= 0.0001:
                    return mid

# calculate using binary solve
f1 = binary_solve(0, 2)

# solution
f2_1 = (-1+sqrt(5))/2
f2_2 = log(f2_1, 2/3)

# display
print('x =', f1)
print('x =', f2_2)
