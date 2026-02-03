# import module
from math import sqrt, log

# 4^x + 6^x = 9^x
def check(x):
    lhs = 4**x + 6**x
    rhs = 9**x
    return lhs - rhs

def solve(left, right):
    # use binary to solve equation
    # return x between left and right
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

if __name__ == "__main__":
    a1 = solve(0, 2)
    a2 = (-1+sqrt(5))/2 # solution
    print('x =', a1)
    print('x =', log(a2, 2/3))

