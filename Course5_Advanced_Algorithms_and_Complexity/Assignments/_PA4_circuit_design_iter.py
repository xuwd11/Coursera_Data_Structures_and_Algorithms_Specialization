# python3
n, m = map(int, input().split())
clauses = [ list(map(int, input().split())) for i in range(m) ]

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

# Types of edges in DFS traversal.
# The numerical values are used in DepthFirstSearcher, change with care.
forward = 1     # traversing edge (v,w) from v to w
reverse = -1    # returning backwards on (v,w) from w to v
nontree = 0     # edge (v,w) is not part of the DFS tree

def search(G):
    """
    Generate sequence of triples (v,w,edgetype) for DFS of graph G.
    The subsequence for each root of each tree in the DFS forest starts
    with (root,root,forward) and ends with (root,root,reverse).
    If the initial vertex is given, it is used as the root and vertices
    not reachable from it are not searched.
    """
    visited = set()
    
    for v in range(len(G)):
        if v not in visited:
            yield v,v,forward
            visited.add(v)
            stack = [(v,iter(G[v]))]
            while stack:
                parent,children = stack[-1]
                try:
                    child = next(children)
                    if child in visited:
                        yield parent,child,nontree
                    else:
                        yield parent,child,forward
                        visited.add(child)
                        stack.append((child,iter(G[child])))
                except StopIteration:
                    stack.pop()
                    if stack:
                        yield stack[-1][0],parent,reverse
            yield v,v,reverse

def postorder(G):
    """Generate all vertices of graph G in depth-first postorder."""
    for v,w,edgetype in search(G):
        if edgetype is reverse:
            yield w


def findSCCs(G, GR):
    post = list(postorder(GR))
    reversePost = post[::-1]
    
    visited = [False] * len(G)
    sccs = []
    sccsIndex = [0] * len(G)
    currIndex = 0
    for v in reversePost:
        scc = set()
        if not visited[v]:
            S = []
            S.append(v)
            #print(S, v, G[v])
            while len(S) > 0:
                v = S.pop()
                if not visited[v]:
                    visited[v] = True
                    scc.add(v)
                    sccsIndex[v] = currIndex
                    for w in G[v]:
                        S.append(w)
            sccs.append(scc)
            #print(sccs)
            currIndex += 1
    #print(sccs)
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
    post = postorder(G)
    for v in post:
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