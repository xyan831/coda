# import module
from math import sqrt
from operator import mul

# vector operations
class vector_class:
    def __init__(self, vec):
        self.vector = vec
        self.magnitude = sqrt(vec[0]**2 + vec[1]**2 + vec[2]**2)
        self.univ = self.get_univ()
    # unit vector
    def get_univ(self):
        x = self.vector[0]/self.magnitude
        y = self.vector[1]/self.magnitude
        z = self.vector[2]/self.magnitude
        return [x, y, z]
    # dot product
    def get_dot(v1, v2):
        return sum(list(map(mul, v1, v2)))
    # cross product
    def get_cross(v1, v2):
        x = v1[1]*v2[2] - v2[1]*v1[2]
        y = -(v1[0]*v2[2] - v2[0]*v1[2])
        z = v1[0]*v2[1] - v2[0]*v1[1]
        return [x, y, z]

# number list operations
class number_list:
    def __init__(self, lst):
        self.lst = lst
        self.lstmax = max(lst)
        self.lstmin = min(lst)
        self.avg = sum(lst)/len(lst)
        self.sd = self.get_sd()
        self.norm = self.get_norm()
    # standard deviation
    def get_sd(self):
        f = []
        for i in self.lst:
            f.append((i-self.avg)**2)
        return (sum(f)/(len(self.lst)-1))**(1/2)
    # normalize btw a and b
    def get_norm(self, a=0, b=1):
        norm = []
        for i in self.lst:
            new = (i-self.lstmin)/(self.lstmax-self.lstmin)
            norm.append((b-a)*new + a)
        return norm

if __name__ == "__main__":
    # vector example
    vec1 = [4,3,2]
    vec2 = [5,7,1]
    f1 = vector_class(vec1)
    print(f1.vector)
    print(f1.magnitude, f1.univ)
    print(vector_class.get_dot(vec1,vec2),vector_class.get_cross(vec1,vec2))
    
    # number list example
    numlist = [1,3,6,3,1]
    f2 = number_list(numlist)
    print(f2.lst)
    print(f2.lstmax, f2.lstmin, f2.avg, f2.sd)
    print(f2.norm)

