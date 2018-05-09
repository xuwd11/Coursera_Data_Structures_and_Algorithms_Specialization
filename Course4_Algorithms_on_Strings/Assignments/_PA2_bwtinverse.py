# python3
import sys
import numpy as np

def InverseBWT(bwt):
    l = len(bwt)
    output = [''] * l
    count = dict()
    shortcut = [0] * l
    byteStart = dict()
    for i in range(l):
        lastChar = bwt[i]
        currCount = count.get(lastChar, 0)
        shortcut[i] = currCount
        count[lastChar] = currCount + 1

    currIndex = 0
    firstCol = []
    for char, currCount in sorted(count.items(), key = lambda x:x[0]):
        firstCol += [char] * currCount
        byteStart[char] = currIndex
        currIndex += currCount

    currIndex = 0
    for i in range(l):
        output[l-i-1] = firstCol[currIndex]
        currIndex = byteStart[bwt[currIndex]] + shortcut[currIndex]
    
    return ''.join(output)

def ibwt(r, *args): #From wiki
    """Inverse Burrows-Wheeler transform. args is the original index \
if it was not indicated by a null byte."""

    firstCol = "".join(sorted(r))
    count = [0]*256
    byteStart = [-1]*256
    #output = [""] * len(r)
    output = []
    shortcut = [None]*len(r)
    #Generates shortcut lists
    for i in range(len(r)):
        shortcutIndex = ord(r[i])
        shortcut[i] = count[shortcutIndex]
        count[shortcutIndex] += 1
        shortcutIndex = ord(firstCol[i])
        if byteStart[shortcutIndex] == -1:
            byteStart[shortcutIndex] = i

    localIndex = (r.index("$") if not args else args[0])
    for i in range(len(r)):
        #takes the next index indicated by the transformation vector
        nextByte = r[localIndex]
        #output [len(r)-i-1] = nextByte
        output.insert(0, nextByte)
        shortcutIndex = ord(nextByte)
        #assigns localIndex to the next index in the transformation vector
        localIndex = byteStart[shortcutIndex] + shortcut[localIndex]
    return "".join(output)

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))