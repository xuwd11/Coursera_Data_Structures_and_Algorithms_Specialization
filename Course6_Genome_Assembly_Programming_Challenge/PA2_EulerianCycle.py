# python3

import sys

class EulerianCycle:
    def __init__(self):
        self.nUnEdges = 0 # number of explored edges
        self.nodesWUE = dict() # key: node with unused edges; value: the position of such node in the current path
        self.path = []
        isBalanced = self._input()
        if not isBalanced:
            print('0')
        else:
            print('1')    
            self.calculateEulerianCycle()
            self.printPath()

    def _input(self):
        data = list(sys.stdin.read().strip().split())
        self.n, self.nUnEdges = int(data[0]), int(data[1])
        self.adj = [[] for _ in range(self.n)]
        self.unusedEdges = [[] for _ in range(self.n)]
        self.outDeg = [0] * self.n
        self.inDeg = [0] * self.n
        self.adjCurPos = [0] * self.n
        for i in range(self.nUnEdges):
            curFrom = int(data[2*i+2])-1
            curTo = int(data[2*i+3])-1
            self.adj[curFrom].append(curTo)
            self.outDeg[curFrom] += 1
            self.inDeg[curTo] += 1
        for i in range(self.n):
            if self.outDeg[i] != self.inDeg[i]:
                return False
        return True
    
    def explore(self, s):
        self.path.append(s)
        curPos = self.adjCurPos[s]
        curMaxPos = self.outDeg[s]
        while curPos < curMaxPos:
            self.adjCurPos[s] = curPos + 1
            if curPos + 1 < curMaxPos:
                self.nodesWUE[s] = len(self.path) - 1
            else:
                if s in self.nodesWUE:
                    del self.nodesWUE[s]
            v = self.adj[s][curPos]
            self.path.append(v)
            s = v
            curPos = self.adjCurPos[s]
            curMaxPos = self.outDeg[s]
            self.nUnEdges -= 1
        return

    def updatePath(self, startPos):
        l = len(self.path) - 1
        self.path = self.path[startPos:l] + self.path[:startPos]
        for node, pos in self.nodesWUE.items():
            if pos < startPos:
                self.nodesWUE[node] = pos + l - startPos
            else:
                self.nodesWUE[node] = pos - startPos
        return

    def calculateEulerianCycle(self):
        self.explore(1)
        while self.nUnEdges > 0:
            node, pos = self.nodesWUE.popitem()
            self.updatePath(pos)
            self.explore(node)
        return self.path

    def printPath(self):
        #print('->'.join([str(node) for node in self.path]))
        print(' '.join([str(node+1) for node in self.path[:-1]]))       

if __name__ == "__main__":
    EulerianCycle()