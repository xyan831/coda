# import module
from random import randint
from math import sqrt, radians, sin, cos, factorial
import numpy as np

# get list of dice rolls
def roll(dice, face):
    # dice = number of dices
    # face = number of faces for each dice
    roll_list = []
    for i in range(dice):
        roll_list.append(randint(1, face))
    return roll_list

# interpolation
def interpolation(xi, x, y):
    # x = [x1, x2], y = [y1, y2]
    # get yi for xi btw [x1, x2]
    p = (y[1]-y[0]) / (x[1]-x[0])
    yi = y[0] + (xi-x[0])*p
    return yi

# get roots of quadratic equation
def quadratic(a, b, c):
    # quadratic equation: (a)x^2 + (b)x + (c) = 0
    q1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    q2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    return [q1, q2]

# matrix solve linear equation
def matrixlinear(a, b):
    # solve: [a][x] = [b] for [x]
    return np.linalg.solve(a, b)

#  euler's formula a*e^(i*t) = a*cos(t) + a*i*sin(t)
def phasor(a, t):
    # a = radius, t = angle
    # get real and imaginary part
    r = a*cos(radians(t))
    i = a*sin(radians(t))
    answer_text = f"{a}e^(i*{t}) = {r:.2e} + i * {i:.2e}"
    return [r, i], answer_text

# counting
def counting(n, r):
    # n = number of elements
    # r = number of permutations/combinations
    # P(n, r) = n! / [(n-r)!]                 permutation
    p = factorial(n)/factorial(n-r)
    # PR(n, r) = n^r                          permutation w/ repetition
    pr = n**r
    # C(n, r) = n! / [r! * (n-r)!]            combination
    c = factorial(n)/(factorial(r)*factorial(n-r))
    # CR(n, r) = (n-1+r)! / [r! * (n-1)!]     combination w/ repetition
    # [CR(n, r) = C(n-1+r, r)]
    cr = factorial(n-1+r)/(factorial(r)*factorial(n-1))
    return p, pr, c, cr

if __name__ == "__main__":
    # roll dice example
    f1 = roll(2,6)
    print(f1)
    
    # interpolation example
    f2_x = [20, 50]
    f2_y = [4321, 33]
    f2 = interpolation(35, f2_x, f2_y)
    print(f2)
    
    # quadratic example: 2x^2 + 3 = 27
    f3 = quadratic(2,0,-24)
    print(f3)
    
    # matrix solve linear eq example
    # 10x + 1y = 180
    # 45x + 1y = 140
    f4_a = [[10,1],[45,1]]
    f4_b = [180,140]
    f4 = matrixlinear(f4_a,f4_b)
    print(f4)
    
    # phasor example: 2*e^(i*60)
    f5_lst, f5_text = phasor(2,60)
    print(f5_lst, f5_text)
    
    # counting example: 34 items in sets of 2
    f6_p, f6_pr, f6_c, f6_cr = counting(34,2)
    print(f6_p, f6_pr, f6_c, f6_cr)

