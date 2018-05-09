#Uses python3

import sys

visited = []
CCnum = []
cc = 0

def number_of_components(adj):
    #write your code here
    result = DFS(adj)
    return result

def explore(adj, v):
    global visited
    global CCnum
    global cc
    visited[v] = True
    CCnum[v] = cc
    for w in adj[v]:
        if not visited[w]:
            explore(adj, w)

def DFS(adj):
    global visited
    global CCnum
    global cc
    visited = [False] * len(adj)
    CCnum = [None] * len(adj)
    cc = 1
    for v in range(len(adj)):
        if not visited[v]:
            explore(adj, v)
            cc += 1
    return cc - 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
