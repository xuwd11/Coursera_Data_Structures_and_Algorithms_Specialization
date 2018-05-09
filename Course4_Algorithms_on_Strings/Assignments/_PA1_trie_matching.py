# python3
import sys

NA = -1

class Node:
	def __init__ (self):
		self.next = [NA] * 4

def build_trie(patterns):
    tree = dict()
    tree[0] = dict()
    newNode = 1
    for pattern in patterns:
        currNode = 0
        l = len(pattern)
        for i in range(l):
            currSymbol = pattern[i]
            if currSymbol in tree[currNode]:
                currNode = tree[currNode][currSymbol]
            else:
                tree[currNode][currSymbol] = newNode
                tree[newNode] = dict()
                currNode = newNode
                newNode += 1                
    return tree

def PrefixTrieMatching(text, tree):
	i = 0
	l = len(text)
	symbol = text[i]
	v = 0
	while True:
		if len(tree[v]) == 0:
			return True
		elif symbol in tree[v]:
			v = tree[v][symbol]
			if i < l-1:
				i += 1
				symbol = text[i]
			elif len(tree[v]) != 0:
				return False
		else:
			return False

def solve (text, n, patterns):
	result = []
	tree = build_trie(patterns)
	#print(tree)
	l = len(text)
	for i in range(l):
		if PrefixTrieMatching(text[i:], tree):
			result.append(i)
	return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
