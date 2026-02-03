# import module
from math import sqrt

# get roots of quadratic equation
def quadratic(a, b, c):
    # quadratic equation: (a)x^2 + (b)x + (c) = 0
    q1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    q2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    return [q1, q2]

if __name__ == "__main__":
    # 2x^2+3=27
    root = quadratic(2,0,-24)
    print(root)

