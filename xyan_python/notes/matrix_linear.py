# import module
import numpy as np

# matrix solve linear equation
def mat_lin_solve(a, b):
    # solve: [a][x] = [b] for [x]
    return np.linalg.solve(a, b)

if __name__ == "__main__":
    #10a+1b=180
    #45a+1b=140
    a = [[10, 1],
        [45, 1]]
    b = [180, 140]
    test1 = mat_lin_solve(a,b)
    print(test1)

