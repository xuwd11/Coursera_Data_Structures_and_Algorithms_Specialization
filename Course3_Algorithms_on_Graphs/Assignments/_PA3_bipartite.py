#Uses python3

import sys
import queue

def bipartite(adj):
    n = len(adj)
    dist = [float('inf')] * n
    color = [None] * n
    cDict = {0:1, 1:0}
    q = queue.Queue()
    q.put(0)
    dist[0] = 0
    color[0] = 0
    while not q.empty():
        u = q.get()
        for v in adj[u]:
            if color[u] == color[v]:
                return 0
            if dist[v] == float('inf'):
                q.put(v)
                dist[v] = dist[u] + 1
                color[v] = cDict[color[u]]
    return 1

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
    print(bipartite(adj))
