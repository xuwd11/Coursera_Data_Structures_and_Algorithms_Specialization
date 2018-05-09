# python3

#import sys, threading
#sys.setrecursionlimit(10**7) # max depth of recursion
#threading.stack_size(2**25)  # new thread will get stack of such size
class TreeHeight:
    def __init__(self, n, parent):
        self.n = n
        self.parent = parent
        self.height = [0]*n
    def computeHeight(self):
        idx = sorted(range(n), key = lambda x: self.parent[x])
        self.height[idx[0]] = 1
        for vertex in range(self.n):
            nodes = []
            i = vertex
            if self.height[i] == 0:
                while True:
                    nodes.append(i)
                    i = self.parent[i]
                    if self.height[i] != 0:
                        nodes.append(i)
                        break
            if nodes:
                for i in range(len(nodes)-2, -1, -1):
                    self.height[nodes[i]] = self.height[nodes[i+1]] + 1
        return max(self.height)

if __name__ == "__main__":
    n = int(input())
    parent = list(map(int, input().split()))
    tree = TreeHeight(n, parent)
    print(tree.computeHeight())