# python3

# Arguments:
#   * `n` - the number of vertices.
#   * `edges` - list of edges, each edge is a tuple (u, v), 1 <= u, v <= n.
#   * `colors` - list consisting of `n` characters, each belonging to the set {'R', 'G', 'B'}.
# Return value: 
#   * If there exists a proper recoloring, return value is a list containing new colors, similar to the `colors` argument.
#   * Otherwise, return value is None.

colorDict = {'R':{'G':0, 'B':1}, 'G':{'R':0, 'B':1}, 'B':{'R':0, 'G':1}}
rcolorDict = {'R':'GB', 'G':'RB', 'B':'RG'}

def varnum(i, k):
    return 2*i+k+1

def colorIndex(j):
    return j // 2, j % 2

def getNode(i):
    # i -> 2*|i|-2 if i > 0
    # i -> 2*|i|-1 if i < 0
    return 2*abs(i)-1-(i>0)

def getAssignment(k):
    if 0 == 1 & k:
        return k//2+1
    else:
        return -k//2

def constructGraph(n, edges, colors):
    clauses = []
    for i in range(n):
        clauses.append((varnum(i, 0), varnum(i, 1)))
        clauses.append((-varnum(i, 0), -varnum(i, 1)))

    for e in edges:
        try:
            clauses.append((-varnum(e[0], colorDict[colors[e[0]]]['R']), -varnum(e[1], colorDict[colors[e[1]]]['R'])))
        except:
            pass
        try:
            clauses.append((-varnum(e[0], colorDict[colors[e[0]]]['G']), -varnum(e[1], colorDict[colors[e[1]]]['G'])))
        except:
            pass
        try:
            clauses.append((-varnum(e[0], colorDict[colors[e[0]]]['B']), -varnum(e[1], colorDict[colors[e[1]]]['B'])))
        except:
            pass
    
    G = [[] for _ in range(4*n)]
    GR = [[] for _ in range(4*n)]

    for clause in clauses:
        G[getNode(-clause[0])].append(getNode(clause[1]))
        G[getNode(-clause[1])].append(getNode(clause[0]))

        GR[getNode(clause[1])].append(getNode(-clause[0]))
        GR[getNode(clause[0])].append(getNode(-clause[1]))
    
    #print(clauses)
    #print(G)
    #print(GR)
    
    return G, GR

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

def assign_new_colors(n, edges, colors):
    G, GR = constructGraph(n, edges, colors)
    sccs, sccsIndex = findSCCs(G, GR)
    #print(sccs, sccsIndex)
    if not checkSatisfication(sccs):
        return None

    result = [False] * (2*n)
    assigned = [False] * len(G)
    post = postorder(G)
    for v in post:
        if not assigned[v]:
            for w in sccs[sccsIndex[v]]:
                if not assigned[w]:
                    result[abs(getAssignment(w))-1] = (getAssignment(w) < 0)
                    assigned[w] = True
                    assigned[getNode(-getAssignment(w))] = True
    newColors = [rcolorDict[colors[i//2]][i%2] for i, r in enumerate(result) if not r]
    return newColors
    
def main():
    n, m = map(int, input().split())
    colors = input()
    edges = set()
    for i in range(m):
        u, v = map(int, input().split())
        if u != v and not (u-1, v-1) in edges and not (v-1, u-1) in edges:
            edges.add((u-1, v-1))
    new_colors = assign_new_colors(n, edges, colors)
    if new_colors is None:
        print("Impossible")
    else:
        print(''.join(new_colors))

main()
