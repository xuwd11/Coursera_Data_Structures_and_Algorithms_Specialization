#Uses python3

import sys
import queue


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    n = len(adj)
    distance[s] = 0
    reachable[s] = 1
    for _ in range(n - 1):
        for u in range(n):
            for i, v in enumerate(adj[u]):
                d = distance[u] + cost[u][i]
                if distance[v] > d:
                    distance[v] = d
                    reachable[v] = 1
    Q = queue.Queue()
    for u in range(n):
        for i, v in enumerate(adj[u]):
            d = distance[u] + cost[u][i]
            if distance[v] > d:
                Q.put(v)
                shortest[v] = 0
    shortest = bfs(adj, Q, shortest)
    return distance, reachable, shortest

def bfs(adj, Q, shortest):
    n = len(adj)
    while not Q.empty():
        u = Q.get()
        for v in adj[u]:
            if shortest[v] == 1:
                shortest[v] = 0
                Q.put(v)
    return shortest
    
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
    s = data[0]
    s -= 1
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    distance, reachable, shortest = shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

