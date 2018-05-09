# python3

import sys
import queue

class BubbleDetection:
    def __init__(self):
        adj = self._input()
        print(self.findBubbles(adj))
        

    def _input(self):
        data = list(sys.stdin.read().strip().split())
        k, t = int(data[0]), int(data[1])
        data = data[2:]
        adj = self.DeBrujin(k, data)
        return adj

    def DeBrujin(self, k, patterns):
        adj = dict()
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
        return adj

    def findBubbles(self, adj):
        bubble = 0
        for v in adj.values():
            if len(v) > 1:
                bubble += 1
        return bubble

if __name__ == "__main__":
    BubbleDetection()