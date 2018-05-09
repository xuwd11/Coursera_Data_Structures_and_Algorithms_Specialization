# python3

import sys

class Rope:
	def __init__(self, s):
		self.s = s
	def result(self):
		return self.s
	def processNaive(self, i, j, k):
        # Write your code here
		s1 = self.s[i:j+1]
		s2 = self.s[0:i] + self.s[j+1:]
		self.s = s2[0:k] + s1 + s2[k:]
                

rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
	i, j, k = map(int, sys.stdin.readline().strip().split())
	rope.processNaive(i, j, k)
print(rope.result())
