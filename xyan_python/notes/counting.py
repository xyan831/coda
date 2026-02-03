# import module
from math import factorial

# count permutations/combinations of element group
def Count(n, r):
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
    ct1_p, ct1_pr, ct1_c, ct1_cr = Count(34,2) # 34 items in sets of 2
    print("permutation: ", ct1_p)
    print("permu w/ repetition: ", ct1_pr)
    print("combination: ", ct1_c)
    print("combo w/ repetition: ", ct1_cr)

