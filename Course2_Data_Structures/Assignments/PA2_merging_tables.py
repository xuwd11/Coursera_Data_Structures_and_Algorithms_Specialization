# python3

n, m = map(int, input().split())
lines = list(map(int, input().split()))
rank = [1] * n
parent = list(range(0, n))

def getParent(table):
    # find parent and compress path
    path = []
    while table != parent[table]:
        path.append(table)
        table = parent[table]
    for i in path:
        parent[i] = table
    return table
    
def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return lines[realSource]
    if rank[realDestination] < rank[realSource]:
        parent[realDestination] = realSource
        lines[realSource] += lines[realDestination]
        return lines[realSource]
    else:
        parent[realSource] = realDestination
        lines[realDestination] += lines[realSource]        
        if rank[realDestination] == rank[realSource]:
            rank[realDestination] += 1
        return lines[realDestination]

    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size

ans = max(lines)

for i in range(m):
    destination, source = map(int, input().split())
    ans = max(ans, merge(destination - 1, source - 1))
    print(ans)