#Uses python3
import sys
import math
import queue

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.regions = n
    
    def find(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
        return i
    
    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        self.regions -= 1
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1

def clustering(x, y, k):
    n = len(x)
    D = DisjointSet(n)
    Q = queue.PriorityQueue()
    for i in range(n):
        for j in range(i+1, n):
            Q.put((distance(x[i], y[i], x[j], y[j]), (i, j)))
    while not Q.empty():
        dist, (u, v) = Q.get()
        if D.find(u) != D.find(v):
            if D.regions == k:
                return dist
            D.union(u, v)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))


'''
class MySet:
    def __init__(self):
        self.regions = 0

    def make_set(self, x):
        x.parent = x
        x.rank   = 0
        self.regions += 1

    def union(self, x, y):
        self.regions -= 1
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot.rank > yRoot.rank:
            yRoot.parent = xRoot
        elif xRoot.rank < yRoot.rank:
            xRoot.parent = yRoot
        elif xRoot != yRoot:
            yRoot.parent = xRoot
            xRoot.rank = xRoot.rank + 1

    def find(self, x):
        if x.parent == x:
           return x
        else:
           x.parent = self.find(x.parent)
           return x.parent

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = False
        self.rank = 0

    def __str__(self):
        parent_x = self.parent and self.parent.x
        parent_y = self.parent and self.parent.y
        return "[%d, %d] parent: [%d, %d], rank: %d" % (self.x, self.y, parent_x, parent_y, self.rank)

class Edge:
    def __init__(self, x_node, y_node):
        self.x_node = x_node
        self.y_node = y_node
        self.distance = self.calculate_distance()

    def __str__(self):
        return "[%d,%d] - [%d,%d]: %f" % (self.x_node.x, self.x_node.y, self.y_node.x, self.y_node.y, self.distance)

    def calculate_distance(self):
        return math.sqrt(math.pow((self.x_node.x - self.y_node.x), 2) + math.pow((self.x_node.y - self.y_node.y ), 2))

def construct_edges(nodes):
    edges = []
    for x_node in nodes:
        for y_node in nodes:
            if x_node != y_node:
                edges.append(Edge(x_node, y_node))

    return sorted(edges, key=lambda edge: edge.distance)

def clustering(x, y, k):
    #write your code here
    my_set = MySet()
    result_edges = []
    nodes = [Node(x_coord, y[index]) for index, x_coord in enumerate(x)]
    [my_set.make_set(node) for node in nodes]

    edges = construct_edges(nodes)
    for edge in edges:
        if my_set.find(edge.x_node) != my_set.find(edge.y_node):

            if my_set.regions == k:
                return edge.distance

            result_edges.append(edge)
            my_set.union(edge.x_node, edge.y_node)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
'''