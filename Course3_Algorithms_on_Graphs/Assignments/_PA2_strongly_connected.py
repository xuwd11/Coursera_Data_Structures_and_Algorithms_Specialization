#Uses python3

import sys

sys.setrecursionlimit(200000)

visited = []
order = []

def reverseGraph(adj):
    n = len(adj)
    adjr = [[] for _ in range(n)]
    for v in range(len(adj)):
        for w in adj[v]:
            adjr[w].append(v)
    return adjr

def explore(adj, v):
    global visited
    visited[v] = True
    for w in adj[v]:
        if not visited[w]:
            explore(adj, w)

def exploreForOrder(adj, v):
    global visited
    global order
    visited[v] = True
    for w in adj[v]:
        if not visited[w]:
            exploreForOrder(adj, w)
    order.insert(0, v)

def toposort(adj):
    global visited
    global order
    visited = [False] * len(adj)
    for v in range(len(adj)):
        if not visited[v]:
            exploreForOrder(adj, v)
    return order

def number_of_strongly_connected_components(adj):
    global visited
    result = 0
    adjr = reverseGraph(adj)
    order = toposort(adjr)
    visited = [False] * len(adj)
    for v in order:
        if not visited[v]:
            explore(adj, v)
            result += 1
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))