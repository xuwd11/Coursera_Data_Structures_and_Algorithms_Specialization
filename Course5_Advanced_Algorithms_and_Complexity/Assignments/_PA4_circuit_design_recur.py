# python3
n, m = map(int, input().split())
clauses = [ list(map(int, input().split())) for i in range(m) ]
import sys

# This solution tries all possible 2^n variable assignments.
# It is too slow to pass the problem.
def isSatisfiable0():
    for mask in range(1<<n):
        result = [ (mask >> i) & 1 for i in range(n) ]
        formulaIsSatisfied = True
        for clause in clauses:
            clauseIsSatisfied = False
            if result[abs(clause[0]) - 1] == (clause[0] < 0):
                clauseIsSatisfied = True
            if result[abs(clause[1]) - 1] == (clause[1] < 0):
                clauseIsSatisfied = True
            if not clauseIsSatisfied:
                formulaIsSatisfied = False
                break
        if formulaIsSatisfied:
            return result
    return None

def getNode(i):
    # i -> 2*i-2 if i > 0
    # i -> 2*i-1 if i < 0
    return 2*abs(i)-1-(i>0)

def getAssignment(k):
    if 0 == 1 & k:
        return k//2+1
    else:
        return -k//2

def constructGraph(G, GR):
    for clause in clauses:
        G[getNode(-clause[0])].append(getNode(clause[1]))
        G[getNode(-clause[1])].append(getNode(clause[0]))

        GR[getNode(clause[1])].append(getNode(-clause[0]))
        GR[getNode(clause[0])].append(getNode(-clause[1]))

sys.setrecursionlimit(200000)

visited = []
order = []

def reverseGraph(adj):
    n = len(adj)
    adjr = [[] for _ in range(n)]
    for v in range(len(adj)):
        for w in adj[v]:
            adjr[w].append(v)
    return adjr

def explore(adj, v):
    global visited
    visited[v] = True
    for w in adj[v]:
        if not visited[w]:
            explore(adj, w)

def exploreForOrder(adj, v):
    global visited
    global order
    if not visited[v]:
        visited[v] = True
        for w in adj[v]:
            if not visited[w]:
                exploreForOrder(adj, w)
        order.insert(0, v)
    #print(order)

def toposort(adj):
    global visited
    global order
    order = []
    visited = [False] * len(adj)
    for v in range(len(adj)):
        if not visited[v]:
            exploreForOrder(adj, v)
            #print(v, order)
    return order

def findSCCs(adj, adjr):
    global visited
    sccs = []
    sccsIndex = [0]*len(adj)
    result = 0
    order = toposort(adjr)
    #print('')
    #print(adj, adjr)
    #print(order)
    visited = [False] * len(adj)
    sccs = []
    sccsIndex = [0] * len(adj)
    currIndex = 0
    for v in order:
        scc = set()
        if not visited[v]:
            S = []
            S.append(v)
            #print(S, v, adj[v])
            while len(S) > 0:
                v = S.pop()
                if not visited[v]:
                    visited[v] = True
                    scc.add(v)
                    sccsIndex[v] = currIndex
                    for w in adj[v]:
                        S.append(w)
            sccs.append(scc)
            #print(sccs)
            currIndex += 1
    return sccs, sccsIndex

def checkSatisfication(sccs):
    for scc in sccs:
        for v in scc:
            if getNode(-getAssignment(v)) in scc:
                return False
    return True

def isSatisfiable():
    G = [[] for _ in range(2*n)]
    GR = [[] for _ in range(2*n)]
    constructGraph(G, GR)
    sccs, sccsIndex = findSCCs(G, GR)
    #print(sccs, sccsIndex)
    if not checkSatisfication(sccs):
        return None
    

    result = [False] * n
    assigned = [False] * len(G)
    reversePost = toposort(G)
    #print(reversePost)
    #print(reversePost)
    while len(reversePost) > 0:
        v = reversePost.pop()
        if not assigned[v]:
            for w in sccs[sccsIndex[v]]:
                if not assigned[w]:
                    result[abs(getAssignment(w))-1] = (getAssignment(w) < 0)
                    assigned[w] = True
                    assigned[getNode(-getAssignment(w))] = True
    
    return result


result = isSatisfiable()
if result is None:
    print("UNSATISFIABLE")
else:
    print("SATISFIABLE");
    print(" ".join(str(-i-1 if result[i] else i+1) for i in range(n)))