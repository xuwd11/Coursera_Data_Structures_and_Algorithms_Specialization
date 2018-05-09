#Uses python3
import numpy as np

def min_dot_product(a, b):
    #write your code here
    res = 0
    a_sorted = sorted(a)
    b_sorted = sorted(b, reverse = True)
    res = np.dot(a_sorted, b_sorted)
    return res

n = int(input())
a = np.array([int(x) for x in input().split()])
b = np.array([int(x) for x in input().split()])
print(min_dot_product(a, b))