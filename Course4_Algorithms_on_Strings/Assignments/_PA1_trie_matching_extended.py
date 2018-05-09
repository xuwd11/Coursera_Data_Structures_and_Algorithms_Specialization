# python3
import sys

class Node:
    def __init__ (self, id, patternEnd):
        self.id = id
        self.patternEnd = patternEnd

def build_trie(patterns):
    tree = dict()
    root = Node(0, False)
    tree[root.id] = dict()
    newNodeID = 1
    for pattern in patterns:
        currNodeID = 0
        l = len(pattern)
        for i in range(l):
            currSymbol = pattern[i]
            if currSymbol in tree[currNodeID]:
                if i == l-1:
                    tree[currNodeID][currSymbol].patternEnd = True
                currNodeID = tree[currNodeID][currSymbol].id
            else:
                if i == l-1:
                    tree[currNodeID][currSymbol] = Node(newNodeID, True)
                else:
                    tree[currNodeID][currSymbol] = Node(newNodeID, False)
                tree[newNodeID] = dict()
                currNodeID = newNodeID
                newNodeID += 1                
    return tree

def PrefixTrieMatching(text, tree):
	i = 0
	l = len(text)
	symbol = text[i]
	v = Node(0, False)
	while True:
		if v.patternEnd:
			return True
		elif symbol in tree[v.id]:
			v = tree[v.id][symbol]
			if i < l-1:
				i += 1
				symbol = text[i]
			elif not v.patternEnd:
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
