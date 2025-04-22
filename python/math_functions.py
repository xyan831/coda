# math functions
# xyan831

from random import randint
from math import sqrt, radians, sin, cos, factorial
import numpy as np

def roll(dice, face):
    """
    roll dices
    dice = number of dices
    face = number of faces for each dice
    return list of dice roll result
    """
    roll_list = []
    for i in range(dice):
        roll_list.append(randint(1, face))
    return roll_list

def interpolation(xi, x, y):
    """
    interpolation
    x = [x1, x2], y = [y1, y2]
    xi = between x1 and x2
    return yi for xi
    """
    p = (y[1]-y[0]) / (x[1]-x[0])
    yi = y[0] + (xi-x[0])*p
    return yi

def quadratic(a, b, c):
    """
    quadratic equation: (a)x^2 + (b)x + (c) = 0
    return roots of equation
    """
    q1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    q2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    return [q1, q2]

def matrixlinear(a, b):
    """
    matrix solve linear equation: [a][x] = [b]
    return [x]
    """
    return np.linalg.solve(a, b)

def phasor(a, t):
    """
    euler's formula a*e^(i*t) = a*cos(t) + a*i*sin(t)
    a = radius
    t = angle
    return real and imaginary part
    """
    r = a*cos(radians(t))
    i = a*sin(radians(t))
    answer_text = f"{a}e^(i*{t}) = {r:.2e} + i * {i:.2e}"
    return [r, i], answer_text

def counting(n, r):
    """
    class for counting
    n = number of elements
    r = number of permutations/combinations
    P(n, r) = n! / [(n-r)!]                 permutation
    PR(n, r) = n^r                          permutation w/ repetition
    C(n, r) = n! / [r! * (n-r)!]            combination
    CR(n, r) = (n-1+r)! / [r! * (n-1)!]     combination w/ repetition
    [CR(n, r) = C(n-1+r, r)]
    """
    p = factorial(n)/factorial(n-r)
    pr = n**r
    c = factorial(n)/(factorial(r)*factorial(n-r))
    cr = factorial(n-1+r)/(factorial(r)*factorial(n-1))
    return p, pr, c, cr

if __name__ == "__main__":
    # roll dice example
    f1 = roll(2,6)
    #print(f1)
    
    # interpolation example
    f2_x = [20, 50]
    f2_y = [4321, 33]
    f2 = interpolation(35, f2_x, f2_y)
    #print(f2)
    
    # quadratic example: 2x^2 + 3 = 27
    f3 = quadratic(2,0,-24)
    #print(f3)
    
    # matrix solve linear eq example
    # 10x + 1y = 180
    # 45x + 1y = 140
    f4_a = [[10,1],[45,1]]
    f4_b = [180,140]
    f4 = matrixlinear(f4_a,f4_b)
    #print(f4)
    
    # phasor example: 2*e^(i*60)
    f5_lst, f5_text = phasor(2,60)
    #print(f5_lst, f5_text)
    
    # counting example: 34 items in sets of 2
    f6_p, f6_pr, f6_c, f6_cr = counting(34,2)
    #print(f6_p, f6_pr, f6_c, f6_cr)

