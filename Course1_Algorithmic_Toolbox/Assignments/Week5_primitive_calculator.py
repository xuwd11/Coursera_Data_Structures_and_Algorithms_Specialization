# Uses python3

def wrong_optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def min_op(n):
    C = []
    C.append(0)
    for i in range(1, n):
        C.append(C[i-1] + 1)
        if ((i+1)%2 == 0) and (C[(i+1)//2-1]+1 < C[i]):
            C[i] = C[(i+1)//2-1]+1
        if ((i+1)%3 == 0) and (C[(i+1)//3-1]+1 < C[i]):
            C[i] = C[(i+1)//3-1]+1
    return C

def optimal_sequence(C):
    n = len(C)-1
    seq = []
    while n > 0:
        seq.insert(0, n+1)
        if ((n+1)%2 == 0) and (C[(n+1)//2-1]+1 == C[n]):
            n = (n+1)//2-1
            continue
        if ((n+1)%3 == 0) and (C[(n+1)//3-1]+1 == C[n]):
            n = (n+1)//3-1
            continue
        if C[n-1] + 1 == C[n]:
            n -= 1
            continue
    seq.insert(0, 1)
    return seq


n = int(input())
C = min_op(n)
seq = optimal_sequence(C)

print(len(seq) - 1)
for x in seq:
    print(x, end=' ')