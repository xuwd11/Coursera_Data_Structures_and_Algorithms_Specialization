# Uses python3
import sys

def lcm(a, b):
    #write your code here
    return a*b

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

