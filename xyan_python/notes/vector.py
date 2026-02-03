# import module
from math import sqrt
from operator import mul

# vector operations
class Vector:
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
    def get_dot(self, v1, v2):
        return sum(list(map(mul, v1, v2)))
    # cross product
    def get_cross(self, v1, v2):
        x = v1[1]*v2[2] - v2[1]*v1[2]
        y = -(v1[0]*v2[2] - v2[0]*v1[2])
        z = v1[0]*v2[1] - v2[0]*v1[1]
        return [x, y, z]

if __name__ == "__main__":
    vec1 = [4,3,2]
    vec2 = [5,7,1]
    f1 = Vector(vec1)
    print(f'vector = {f1.vector}')
    print(f'magnitude = {f1.magnitude:.2e}')
    print(f"unit vector = {f1.univ}")
    print(f"dot = {f1.get_dot(vec1,vec2)}")
    print(f"cross = {f1.get_cross(vec1,vec2)}")

