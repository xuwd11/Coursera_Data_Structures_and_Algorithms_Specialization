# Uses python3
import sys
import numpy as np

def get_optimal_value(n, capacity, weights, values):
    value = 0.
    # write your code here
    vpw_sorted, weights_sorted, values_sorted = sortVpw(weights, values)
    i = 0
    while capacity >= 0 and i < n:
        a = min(capacity, weights_sorted[i])
        value = value + a*vpw_sorted[i]
        i = i+1
        capacity = capacity - a            
    return value

def sortVpw(weights, values):
    vpw = values/weights
    ind = sorted(range(len(vpw)), reverse = True, key=vpw.__getitem__)
    vpw_sorted = vpw[ind]
    weights_sorted = weights[ind]
    values_sorted = values[ind]
    return vpw_sorted, weights_sorted, values_sorted

n, capacity = list(map(int, input().split()))
data = []
for i in range(n):
    data.append([int(x) for x in input().split()])
data = np.array(data)
values = data[:,0]
weights = data[:,1]

opt_value = get_optimal_value(n, capacity, weights, values)
print("{:.10f}".format(opt_value))