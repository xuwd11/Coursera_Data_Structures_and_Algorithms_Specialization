#Uses python3

import sys

visited = []
recStack = []

def isCyclicUtil(adj, v):
    global visited
    global recStack
    if not visited[v]:
        visited[v] = True
        recStack[v] = True
        for w in adj[v]:
            if (not visited[w]) and isCyclicUtil(adj, w):
                return True
            elif recStack[w]:
                return True
    recStack[v] = False
    return False

def isCyclic(adj):
    global visited
    global recStack
    visited = [False] * len(adj)
    recStack = [False] * len(adj)
    for v in range(len(adj)):
        if isCyclicUtil(adj, v):
            return 1 #True
    return 0 #False

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(isCyclic(adj))