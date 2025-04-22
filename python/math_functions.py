# math functions
# xyan831

from random import randint
import numpy as np
from math import sqrt, radians, sin, cos, factorial
from operator import mul

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

class vector_class:
    """
    class for vector [x, y, z]
    mag = magnitude
    univ = unit vector
    get_dot() = get dot product
    get_cross() = get cross product
    """
    def __init__(self, vec):
        self.vector = vec
        self.mag = sqrt(vec[0]**2 + vec[1]**2 + vec[2]**2)
        self.univ = self.get_univ()
    def get_univ(self):
        x = self.vector[0]/self.mag
        y = self.vector[1]/self.mag
        z = self.vector[2]/self.mag
        return [x, y, z]
    def get_dot(self, v1, v2):
        return sum(list(map(mul, v1, v2)))
    def get_cross(self, v1, v2):
        x = v1[1]*v2[2] - v2[1]*v1[2]
        y = -(v1[0]*v2[2] - v2[0]*v1[2])
        z = v1[0]*v2[1] - v2[0]*v1[1]
        return [x, y, z]

class number_class:
    """
    class for number list
    maxmin = [max, min] of list
    avg = average(mean) of list
    sd = standard deviation of list
    norm = normalize list between (0,1)
    get_sd() = get standerd deviation of list
    get_norm() = get normalize list btw 2 number
    """
    def __init__(self, lst):
        self.lst = lst
        self.maxmin = [max(lst),min(lst)]
        self.avg = sum(lst)/len(lst)
        self.sd = self.get_sd()
        self.norm = self.get_norm()
    def get_sd(self):
        f = []
        for i in self.lst:
            f.append((i-self.avg)**2)
        return (sum(f)/(len(self.lst)-1))**(1/2)
    def get_norm(self, a=0, b=1):
        norm = []
        for i in self.lst:
            new = (i-self.maxmin[1])/(self.maxmin[0]-self.maxmin[1])
            norm.append((b-a)*new + a)
        return norm

class count_class:
    """
    class for counting
    n = number of elements
    r = number of permutations/combinations
    permutation: P(n, r) = n! / [(n-r)!]
    permutation with repetition: PR(n, r) = n^r
    combination: C(n, r) = n! / [r! * (n-r)!]
    combination with repetition:
    CR(n, r) = C(n-1+r, r) = (n-1+r)! / [r! * (n-1)!]
    """
    def __init__(self, n, r):
        self.n = n
        self.r = r
        self.P = factorial(n) / factorial(n-r)
        self.PR = n**r
        self.C = factorial(n) / (factorial(r)*factorial(n-r))
        self.CR = factorial(n-1+r) / (factorial(r)*factorial(n-1))

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
    
    # vector example
    f6_vec1 = [4,3,2]
    f6_vec2 = [5,7,1]
    f6 = vector_class(f6_vec1)
    #print(f6.vector, f6.mag, f6.univ)
    #print(f6.get_dot(f6_vec1,f6_vec2))
    #print(f6.get_cross(f6_vec1,f6_vec2))
    
    # number list example
    f7_list = [1,3,6,3,1]
    f7 = number_class(f7_list)
    #print(f7.lst)
    #print(f7.maxmin, f7.avg, f7.sd)
    #print(f7.norm)
    
    # counting example: 34 items in sets of 2
    f8 = count_class(34,2)
    #print(f8.P, f8.PR, f8.C, f8.CR)
