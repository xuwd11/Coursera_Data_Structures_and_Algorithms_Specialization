# python3
from itertools import permutations
from itertools import combinations
INF = 10 ** 9

def read_data():
    n, m = map(int, input().split())
    graph = [[INF] * n for _ in range(n)]
    for _ in range(m):
        u, v, weight = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = graph[v][u] = weight
    return graph

def print_answer(path_weight, path):
    print(path_weight)
    if path_weight == -1:
        return
    print(' '.join(map(str, path)))

def optimal_path_bf(graph):
    # This solution tries all the possible sequences of stops.
    # It is too slow to pass the problem.
    # Implement a more efficient algorithm here.
    n = len(graph)
    best_ans = INF
    best_path = []

    for p in permutations(range(n)):
        cur_sum = 0
        for i in range(1, n):
            if graph[p[i - 1]][p[i]] == INF:
                break
            cur_sum += graph[p[i - 1]][p[i]]
        else:
            if graph[p[-1]][p[0]] == INF:
                continue
            cur_sum += graph[p[-1]][p[0]]
            if cur_sum < best_ans:
                best_ans = cur_sum
                best_path = list(p)

    if best_ans == INF:
        return (-1, [])
    return (best_ans, [x + 1 for x in best_path])

def optimal_path(graph):
    n = len(graph)
    C = [[INF for _ in range(n)] for __ in range(1<<n)]
    backtrack = [[(-1, -1) for _ in range(n)] for __ in range(1<<n)]
    C[1][0] = 0
    for size in range(1, n):
        for S in combinations(range(n), size):
            S = (0,) + S
            k = sum([1<<i for i in S])
            for i in S:
                if 0 != i:
                    for j in S:
                        if j != i:
                            curr = C[k^(1<<i)][j]+graph[i][j]
                            if curr < C[k][i]:
                                C[k][i] = curr
                                backtrack[k][i] = (k^(1<<i), j)
    
    bestAns, currIndex2 = min([(C[(1<<n)-1][i]+graph[0][i], i) for i in range(n)])
    
    if bestAns >= INF:
        return (-1, [])
    
    bestPath = []
    currIndex1 = (1<<n)-1
    while -1 != currIndex1:
        bestPath.insert(0, currIndex2+1)
        currIndex1, currIndex2 = backtrack[currIndex1][currIndex2]
    return (bestAns, bestPath)

if __name__ == '__main__':
    print_answer(*optimal_path(read_data()))
