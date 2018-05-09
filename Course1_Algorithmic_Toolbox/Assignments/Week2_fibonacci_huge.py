# Uses python3

def get_fibonaccihuge(n, m):
    fibPrev = 0
    fib = 1
    cached = [fibPrev, fib]

    for i in range(n):
        fibOld = fib
        fib = (fibPrev + fib) % m
        fibPrev = fibOld
        if fibPrev == 0 and fib == 1:
            cached.pop()
            break
        else:
            cached.append(fib)

    return cached[n % len(cached)]


n, m = map(int, input().split())
print(get_fibonaccihuge(n, m))