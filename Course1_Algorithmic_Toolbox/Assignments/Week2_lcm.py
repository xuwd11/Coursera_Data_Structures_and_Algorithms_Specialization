# Uses python3

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    #write your code here
    return int(a/gcd(a, b))*b

a, b = map(int, input().split())
print(lcm(a, b))