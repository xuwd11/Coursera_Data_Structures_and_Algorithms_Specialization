# Uses python3
'''
import sys

input = sys.stdin.read()
tokens = input.split()
a = int(tokens[0])
b = int(tokens[1])
print(a + b)
'''
a = [int(x) for x in input().split()]
print(a[0] + a[1])