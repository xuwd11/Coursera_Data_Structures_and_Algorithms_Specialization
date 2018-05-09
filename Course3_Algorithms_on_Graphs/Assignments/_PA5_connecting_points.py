#Uses python3
import sys
import math
import queue

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def minimum_distance(x, y):
    result = 0.
    n = len(x)
    cost = [float('inf')] * n
    #parent = [None] * n
    cost[0] = 0
    Q = queue.PriorityQueue()
    Q.put((0, 0))
    processed = set()
    while not Q.empty():
        d, v = Q.get()
        if v not in processed:
            result += d
            processed.add(v)
            for z in range(n):
                if z not in processed:
                    currCost = distance(x[v], y[v], x[z], y[z])
                    if cost[z] > currCost:
                        cost[z] = currCost
                        #parent[z] = v
                        Q.put((currCost, z))
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
