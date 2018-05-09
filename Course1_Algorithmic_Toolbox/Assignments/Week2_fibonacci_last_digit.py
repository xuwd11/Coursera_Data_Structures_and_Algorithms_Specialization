# Uses python3

def get_fibonacci_last_digit(n):
    if (n <= 1):
        return n
    else:
        f = [None]*(n+1)
        f[0] = 0
        f[1] = 1
        for i in range(2, n+1):
            f[i] = (f[i-1]+f[i-2])%10
    return f[n]

n = int(input())
print(get_fibonacci_last_digit(n))
