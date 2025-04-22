# math classes
# xyan831

from math import sqrt
from operator import mul

class vector_class:
    """
    class for vector [x, y, z]
    vec = vector
    mag = magnitude
    uv = unit vector
    get_dot() = get dot product
    get_cross() = get cross product
    """
    def __init__(self, vec):
        self.vector = vec
        self.mag = sqrt(vec[0]**2 + vec[1]**2 + vec[2]**2)
        self.uv = self.get_univ()
    def get_univ(self):
        x = self.vector[0]/self.mag
        y = self.vector[1]/self.mag
        z = self.vector[2]/self.mag
        return [x, y, z]
    def get_dot(v1, v2):
        return sum(list(map(mul, v1, v2)))
    def get_cross(v1, v2):
        x = v1[1]*v2[2] - v2[1]*v1[2]
        y = -(v1[0]*v2[2] - v2[0]*v1[2])
        z = v1[0]*v2[1] - v2[0]*v1[1]
        return [x, y, z]

class number_list:
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

if __name__ == "__main__":
    # vector example
    vec1 = [4,3,2]
    vec2 = [5,7,1]
    f1 = vector_class(vec1)
    #print(f1.vector)
    #print(f1.mag, f1.uv)
    #print(vector_class.get_dot(vec1,vec2),vector_class.get_cross(vec1,vec2))
    
    # number list example
    numlist = [1,3,6,3,1]
    f2 = number_list(numlist)
    #print(f2.lst)
    #print(f2.maxmin, f2.avg, f2.sd)
    #print(f2.norm)

