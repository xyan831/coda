# import module
from math import sin, cos, radians

#  euler's formula a*e^(i*t) = a*cos(t) + a*i*sin(t)
def phasor(a, t):
    # a = radius, t = angle
    # get real and imaginary part
    r = a*cos(radians(t))
    i = a*sin(radians(t))
    answer_text = f"{a}e^(i*{t}) = {r:.2e} + i * {i:.2e}"
    return [r, i], answer_text

if __name__ == "__main__":
    a = 2
    t = 60
    p, ans = phasor(a,t) # a*e^(i*t)
    print(ans)

