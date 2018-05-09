#Uses python3

import sys
import queue


def distance(adj, cost, s, t):
    n = len(adj)
    dist = [float('inf')] * n
    prev = [None] * n
    dist[s] = 0
    H = queue.PriorityQueue()
    H.put((0, s))
    processed = set()
    while not H.empty():
        _, u = H.get()
        if u == t:
            return dist[u]
        if u not in processed:
            processed.add(u)
            for i, v in enumerate(adj[u]):
                d = dist[u] + cost[u][i]
                if dist[v] > d:
                    dist[v] = d
                    prev[v] = u
                    H.put((d, v))
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))