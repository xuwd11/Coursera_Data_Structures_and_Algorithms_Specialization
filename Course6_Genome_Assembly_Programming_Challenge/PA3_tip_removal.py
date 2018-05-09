# python3

import sys
import queue

class TipRmoval:
    def __init__(self):
        adj, inDeg, outDeg = self._input()
        print(self.countTips(adj, inDeg, outDeg))
        

    def _input(self):
        data = list(sys.stdin.read().strip().split())
        k = int(data[0])
        data = data[1:]
        adj = self.DeBrujin(k, data)
        return adj

    def DeBrujin(self, k, patterns):
        adj = dict()
        inDeg = dict()
        outDeg = dict()
        for p in patterns:
            l = len(p)
            for i in range(l-k+1):
                if p[i:i+k-1] in adj:
                    adj[p[i:i+k-1]][p[i+1:i+k]] = adj[p[i:i+k-1]].get(p[i+1:i+k], 0) + 1
                else:
                    adj[p[i:i+k-1]] = dict()
                    adj[p[i:i+k-1]][p[i+1:i+k]] = 1
                if p[i+1:i+k] not in adj:
                    adj[p[i+1:i+k]] = dict()
                if not p[i:i+k-1] in inDeg:
                    inDeg[p[i:i+k-1]] = 0
                if not p[i:i+k-1] in outDeg:
                    outDeg[p[i:i+k-1]] = 0
                if not p[i+1:i+k] in inDeg:
                    inDeg[p[i+1:i+k]] = 0
                if not p[i+1:i+k] in outDeg:
                    outDeg[p[i+1:i+k]] = 0
                inDeg[p[i+1:i+k]] += 1
                outDeg[p[i:i+k-1]] += 1
                
        return adj, inDeg, outDeg

    def countTips(self, adj, inDeg, outDeg):
        tip = 0
        for v in inDeg.keys():
            if 0 == inDeg[v] or 0 == outDeg[v]:
                tip += 1
        return tip

if __name__ == "__main__":
    TipRmoval()