# Uses python3
import numpy as np

def optimal_points(segments):
    a = segments[:,0]
    b = segments[:,1]
    ind = sorted(range(len(b)), key=b.__getitem__)
    a_sorted = a[ind]
    b_sorted = b[ind]
    points = [b_sorted[0]]
    for i in range(1, len(ind)):
        if a_sorted[i] > points[-1]:
            points.append(b_sorted[i])
    return points

n = int(input())
data = []
for i in range(n):
    data.append([int(x) for x in input().split()])
segments = np.array(data)
points = optimal_points(segments)
print(len(points))
for p in points:
    print(p, end=' ')
