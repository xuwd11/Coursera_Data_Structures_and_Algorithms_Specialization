# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    else:
        f = [None]*(n+1)
        f[0] = 0
        f[1] = 1
        for i in range(2, n+1):
            f[i] = f[i-1]+f[i-2]
    return f[n]

n = int(input())
print(calc_fib(n))