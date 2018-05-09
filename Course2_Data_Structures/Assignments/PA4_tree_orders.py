# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    s = []
    node = 0
    while s or node != -1:
      if node != -1:
        s.append(node)
        node = self.left[node]
      else:
        node = s.pop()
        self.result.append(self.key[node])
        node = self.right[node]            
    return self.result

  def preOrder(self):
    self.result = []
    s = []
    node = 0
    s.append(node)
    while s:
      node = s.pop()
      self.result.append(self.key[node])
      if self.right[node] != -1:
        s.append(self.right[node])
      if self.left[node] != -1:
        s.append(self.left[node])
    return self.result

  def postOrder(self):
    self.result = []
    s = []
    node = 0
    lastNodeVisited = -1
    while s or node != -1:
      if node != -1:
        s.append(node)
        node = self.left[node]
      else:
        peekNode = s[-1]
        if self.right[peekNode] != -1 and lastNodeVisited != self.right[peekNode]:
          node = self.right[peekNode]
        else:
          self.result.append(self.key[peekNode])
          lastNodeVisited = s.pop()            
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
