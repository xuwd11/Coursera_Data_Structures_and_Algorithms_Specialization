# python3
import sys

class FindPattern:
    """
    Find all the occurrences of the pattern in the text
    and return a list of all positions in the text
    where the pattern starts in the text.
    """
    def __init__(self):
        self._input()
        result = self.findAllOccurrences(self.pattern, self.text)
        print(" ".join(map(str, result)))
    
    def _input(self):
        pattern = sys.stdin.readline().strip()
        text = sys.stdin.readline().strip()
        self.pattern = pattern
        self.text = text
    
    def computePrefixFunction(self, P):
        l = len(P)
        s = [0] * l
        border = 0
        for i in range(1, l):
            while border > 0 and P[i] != P[border]:
                border = s[border-1]
            if P[i] == P[border]:
                border += 1
            else:
                border = 0
            s[i] = border
        return s
    
    def findAllOccurrences(self, pattern, text):
        string = pattern + '$' + text
        s = self.computePrefixFunction(string)
        result = []
        for i in range(len(pattern) + 1, len(string)):
            if s[i] == len(pattern):
                result.append(i - 2*len(pattern))
        return result

if __name__ == '__main__':
    FindPattern()