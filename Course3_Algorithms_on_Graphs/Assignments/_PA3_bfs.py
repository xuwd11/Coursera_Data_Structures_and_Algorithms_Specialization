#Uses python3

import sys
import queue

def distance(adj, s, t):
    if s == t:
        return 0
    n = len(adj)
    dist = [float('inf')] * n
    dist[s] = 0
    q = queue.Queue()
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in adj[u]:
            if dist[v] == float('inf'):
                q.put(v)
                dist[v] = dist[u] + 1
                if v == t:
                    return dist[v]
    return -1

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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
