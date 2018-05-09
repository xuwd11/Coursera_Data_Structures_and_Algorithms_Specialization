# python3
import sys

class SuffixTreeNode:
    def __init__(self, children, parent, stringDepth, edgeStart, edgeEnd):
        self.children = children
        self.parent = parent
        self.stringDepth = stringDepth
        self.edgeStart = edgeStart
        self.edgeEnd = edgeEnd

def createNewLeaf(node, S, suffix):
    leaf = SuffixTreeNode(dict(), node, len(S)-suffix, suffix+node.stringDepth, len(S)-1)
    node.children[S[leaf.edgeStart]] = leaf
    #print(node.id, node.edgeStart, S[node.edgeStart], node.children.items())
    return leaf

def breakEdge(node, S, start, offset):
    startChar = S[start]
    midChar = S[start + offset]
    
    #midNode = SuffixTreeNode(dict(), node, node.stringDepth+offset, start+offset, node.children[startChar].edgeEnd)
    midNode = SuffixTreeNode(dict(), node, node.stringDepth + offset, start, start + offset - 1)
    midNode.children[midChar] = node.children[startChar]
    node.children[startChar].parent = midNode
    node.children[startChar] = midNode
    midNode.children[midChar].edgeStart += offset
    return midNode

def suffix_array_to_suffix_tree(sa, lcp, S):
    root = SuffixTreeNode(children = dict(), parent = None, stringDepth = 0, edgeStart = -1, edgeEnd = -1)
    lcpPrev = 0
    currNode = root
    for i in range(len(S)):
        #print(i)
        suffix = sa[i]
        while currNode.stringDepth > lcpPrev:
            currNode = currNode.parent
        if currNode.stringDepth == lcpPrev:
            leaf = createNewLeaf(currNode, S, suffix)
        else:
            edgeStart = sa[i-1] + currNode.stringDepth
            offset = lcpPrev - currNode.stringDepth
            midNode = breakEdge(currNode, S, edgeStart, offset)
            leaf = createNewLeaf(midNode, S, suffix)
        currNode = leaf
        if i < len(S) - 1:
            lcpPrev = lcp[i]
    return root


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    sa = list(map(int, sys.stdin.readline().strip().split()))
    lcp = list(map(int, sys.stdin.readline().strip().split()))
    print(text)
    root = suffix_array_to_suffix_tree(sa, lcp, text)
    stack = [(root, 0)]
    result_edges = []
    while len(stack) > 0:
        (node, edge_index) = stack[-1]
        stack.pop()
        if 0 == len(node.children):
            continue
        edges = sorted(node.children.keys())
        if edge_index + 1 < len(edges):
            stack.append((node, edge_index + 1))
        print("%d %d" % (node.children[edges[edge_index]].edgeStart, node.children[edges[edge_index]].edgeEnd + 1))
        stack.append((node.children[edges[edge_index]], 0))
