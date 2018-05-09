# python3

import re
def read_input():
    return (input().rstrip(), input().rstrip())

def _hash_func(S,p,x): 
    ans = 0 
    for c in reversed(S):
        ans = (ans * x + ord(c)) % p
    return ans

def print_occurrences(output):
    print(' '.join(map(str, output)))

def precompute_hashes(text, n, p, x):
    H = [None]*(len(text)-n+1)
    S = text[len(text)-n:len(text)]
    H[len(text)-n] = _hash_func(S,p,x)
    y = 1
    for i in range(n):
        y = (y*x) % p
    for i in range(len(text)-n-1, -1, -1):
        H[i] = (x*H[i+1]+ord(text[i])-y*ord(text[i+n])) % p
    return H

def get_occurrences(pattern, text):
    '''
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]
    return [m.start() for m in re.finditer('(?='+pattern+')', text)]
    '''
    x = 263
    p = 1000000007 
    result = []
    n = len(pattern)
    pHash = _hash_func(pattern, p, x)
    H = precompute_hashes(text, n, p, x)
    for i in range(len(text)-n+1):
        if pHash != H[i]:
            continue
        if text[i:i+n] == pattern:
            result.append(i)
    return result    

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

