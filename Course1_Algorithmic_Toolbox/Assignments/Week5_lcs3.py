#Uses python3

def lcs3(a, b, c):
    C = [([([0]*(len(c)+1)) for rowb in range(len(b)+1)]) for rowa in range(len(a)+1)]
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            for k in range(1, len(c)+1):
                if (a[i-1] == b[j-1]) and (b[j-1] == c[k-1]):
                    C[i][j][k] = C[i-1][j-1][k-1] + 1
                else:
                    C[i][j][k] = max(C[i-1][j-1][k-1], C[i-1][j-1][k], C[i-1][j][k-1], C[i-1][j][k], C[i][j-1][k-1], C[i][j-1][k], C[i][j][k-1]) 
    return C[len(a)][len(b)][len(c)]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    l = int(input())
    c = list(map(int, input().split()))
    print(lcs3(a, b, c))