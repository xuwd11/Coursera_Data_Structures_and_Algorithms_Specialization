import logging
import random

#import _PA4_circuit_design

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)


def is_satisfiable(n, m, clauses):
    for mask in range(1 << n):
        result = [(mask >> i) & 1 for i in range(n)]
        formulaIsSatisfied = True
        for clause in clauses:
            clause_is_satisfied = False
            if result[abs(clause[0]) - 1] == (clause[0] < 0):
                clause_is_satisfied = True
            if result[abs(clause[1]) - 1] == (clause[1] < 0):
                clause_is_satisfied = True
            if not clause_is_satisfied:
                formulaIsSatisfied = False
                break
        if formulaIsSatisfied:
            return result



def getNode(i):
    # i -> 2*i-2 if i > 0
    # i -> 2*i-1 if i < 0
    return 2*abs(i)-1-(i>0)

def getAssignment(k):
    if 0 == 1 & k:
        return k//2+1
    else:
        return -k//2

def constructGraph(G, GR, clauses):
    for clause in clauses:
        G[getNode(-clause[0])].append(getNode(clause[1]))
        G[getNode(-clause[1])].append(getNode(clause[0]))

        GR[getNode(clause[1])].append(getNode(-clause[0]))
        GR[getNode(clause[0])].append(getNode(-clause[1]))

def dfs(G):
    pre = [-1] * len(G)
    post = [-1] * len(G)
    preCount = 0
    postCount = 0
    S = []
    for v in range(len(G)):
        #rp = []
        S.append(v)
        while S:
            u = S.pop()
            if post[u] > -1:
                continue
            elif pre[u] > -1:
                post[u] = postCount
                postCount += 1
            else:
                S.append(u)
                pre[u] = preCount
                preCount += 1
                for v in G[u]:
                    if -1 == pre[v]:
                        S.append(v)
    return post

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
    #reversePost = dfs(GR)
    #print(G, GR)
    #print(reversePost)
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
            while len(S) > 0:
                v = S.pop()
                if not visited[v]:
                    visited[v] = True
                    scc.add(v)
                    sccsIndex[v] = currIndex
                    for w in G[v]:
                        S.append(w)
            sccs.append(scc)
            currIndex += 1
    #print(sccs)
    return sccs, sccsIndex

def checkSatisfication(sccs):
    for scc in sccs:
        for v in scc:
            if getNode(-getAssignment(v)) in scc:
                return False
    return True

def isSatisfiable(n, m, clauses):
    G = [[] for _ in range(2*n)]
    GR = [[] for _ in range(2*n)]
    constructGraph(G, GR, clauses)
    sccs, sccsIndex = findSCCs(G, GR)
    #print(sccs, sccsIndex)
    if not checkSatisfication(sccs):
        return None

    result = [False] * n
    assigned = [False] * len(G)
    reversePost = dfs(G)
    while len(reversePost) > 0:
        v = reversePost.pop()
        if not assigned[v]:
            for w in sccs[sccsIndex[v]]:
                if not assigned[w]:
                    result[abs(getAssignment(w))-1] = (getAssignment(w) < 0)
                    assigned[w] = True
                    assigned[getNode(-getAssignment(w))] = True
    return result

def main():
    n = random.randint(1, 10)
    m = random.randint(1, 10)
    clauses = []
    LOG.info('n: %s m: %s', n, m)
    choices = list(range(-n, 0)) + list(range(1, n + 1))
    l = len(choices)

    for __ in range(m):
        a = 0
        b = 0
        while(a == b):
            a = choices[random.randint(0, l - 1)]
            b = choices[random.randint(0, l - 1)]
        clauses.append([a, b])

    expected = is_satisfiable(n, m, clauses) is not None

    try:
        result = isSatisfiable(n, m, clauses) is not None
        #print(expected, result)
    except Exception as e:
        LOG.exception(e)
        result = not expected
    
    '''
    assert expected == result, (
        'expected: {0} result: {1} clauses: {2}'.format(
            expected, result, '\n'.join([' '.join([str(v) for v in clause]) for clause in clauses]),
        )
    )
    '''
    if expected != result:
        print(n, m)
        print('\n'.join([' '.join([str(v) for v in clause]) for clause in clauses]))
        print('')
        print(is_satisfiable(n, m, clauses))
        print('')
        print(isSatisfiable(n, m, clauses))
        print('')
        print(0/0)


if __name__ == '__main__':
    while True:
        main()
