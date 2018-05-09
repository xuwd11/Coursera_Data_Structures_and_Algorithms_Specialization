#Uses python3

import sys

visited = []
order = []

def explore(adj, v):
    global visited
    global order
    visited[v] = True
    for w in adj[v]:
        if not visited[w]:
            explore(adj, w)
    order.insert(0, v)

def toposort(adj):
    global visited
    global order
    visited = [False] * len(adj)
    for v in range(len(adj)):
        if not visited[v]:
            explore(adj, v)
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    print(' '.join([str(i+1) for i in order]))