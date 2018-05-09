#Uses python3

import sys


def negative_cycle(adj, cost):
    n = len(adj)
    adj.append(range(n))
    cost.append([0] * n)
    dist = [float('inf')] * (n + 1)
    prev = [None] * (n + 1)
    dist[n] = 0
    for _ in range(n):
        for u in range(n + 1):
            for i, v in enumerate(adj[u]):
                d = dist[u] + cost[u][i]
                if dist[v] > d:
                    dist[v] = d
                    prev[v] = u
    for u in range(n + 1):
        for i, v in enumerate(adj[u]):
            d = dist[u] + cost[u][i]
            if dist[v] > d:
                return 1
    return 0


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
    print(negative_cycle(adj, cost))
