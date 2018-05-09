# Uses python3

def optimal_weight(W, w):
    v = [([0]*(len(w)+1)) for row in range(W+1)]
    for i in range(1, len(w)+1):
        for weight in range(1, W+1):
            v[weight][i] = v[weight][i-1]
            if w[i-1] <= weight:
                val = v[weight-w[i-1]][i-1] + w[i-1]
                if val > v[weight][i]:
                    v[weight][i] = val
    return v[W][len(w)]

    

W, n = list(map(int, input().split()))
w = list(map(int, input().split()))
print(optimal_weight(W, w))
