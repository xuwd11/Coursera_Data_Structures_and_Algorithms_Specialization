#python3
#This implementation generated wrong answers in some cases; reasons not identified.

import sys
from ctypes import *
import copy

class Node:
    def __init__(self, start, end, suffixLink = None):
        self.start = start
        self.end = end
        self.children = dict()
        self.suffixLink = suffixLink
        self.suffixIndex = -1
    
    def edgeLength(self):
        return self.end[0] - self.start + 1

class SuffixTree:
    def __init__(self, text):
        self.text = text
        self.size = len(text)
        self.remainingSuffixCount = 0

        self.buildSuffixTree(text)

    def walkDown(self, currNode):
        edgeLength = currNode.edgeLength()
        if self.activeLength >= edgeLength:
            self.activeEdge += edgeLength
            self.activeLength -= edgeLength
            self.activeNode = currNode
            return True
        return False
    
    def buildSuffixTree(self, text):
        self.leafEnd = pointer(c_int(-1))
        rootEnd = pointer(c_int(-1))
        self.root = Node(-1, rootEnd)
        self.activeNode = self.root
        self.activeLength = 0
        self.activeEdge = -1
        for i in range(self.size):
            self.extendSuffixTree(i, text)
        labelHeight = 0
        self.setSuffixIndexByDFS(self.root, labelHeight)
        
    def extendSuffixTree(self, pos, text):
        self.leafEnd[0] = pos
        self.remainingSuffixCount += 1
        lastNewNode = None
        while self.remainingSuffixCount > 0:
            if self.activeLength == 0:
                self.activeEdge = pos
            if not text[self.activeEdge] in self.activeNode.children:
                self.activeNode.children[text[self.activeEdge]] = Node(pos, self.leafEnd, self.root)
                if lastNewNode != None:
                    lastNewNode.suffixLink = self.activeNode
                    lastNewNode = None
            else:
                next = self.activeNode.children[text[self.activeEdge]]
                if self.walkDown(next):
                    continue
                if text[next.start + self.activeLength] == text[pos]:
                    if lastNewNode != None and self.activeNode != self.root:
                        lastNewNode.suffixLink = self.activeNode
                        lastNewNode = None
                    self.activeLength += 1
                    break
                splitEnd = pointer(c_int(-1))
                splitEnd[0] = next.start + self.activeLength - 1
                split = Node(next.start, splitEnd, self.root)
                self.activeNode.children[text[self.activeEdge]] = split
                split.children[text[pos]] = Node(pos, self.leafEnd, self.root)
                next.start += self.activeLength
                split.children[text[next.start]] = next
                if lastNewNode != None:
                    lastNewNode.suffixLink = split
                lastNewNode = split
            self.remainingSuffixCount -= 1
            if self.activeNode == self.root and self.activeLength>0:
                self.activeLength -= 1
                self.activeEdge = pos - self.remainingSuffixCount + 1
            elif self.activeNode != self.root:
                self.activeNode = self.activeNode.suffixLink
    
    def setSuffixIndexByDFS(self, node, labelHeight):
        text = self.text
        if node == None:
            return
        if node.start != -1:
            print(text[node.start:node.end[0]+1])
        leaf = True
        for n in node.children.values():
            #if leaf and node.start != -1:
                #print(node.suffixIndex)
            leaf = False
            self.setSuffixIndexByDFS(n, labelHeight + n.edgeLength())
        if leaf:
            node.suffixIndex = self.size - labelHeight
            #print(node.suffixIndex)
            
if __name__ == "__main__":
    SuffixTree(input())