# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

'''
for i in range(0, n):
    for j in range(i+1, n):
        if a[i]*a[j] > result:
            result = a[i]*a[j]

print(result)
'''
maxIdx1 = -1
maxIdx2 = -1
for i in range(0, n):
    if maxIdx1 == -1 or a[i] > a[maxIdx1]:
        maxIdx1 = i
for j in range(0, n):
    if j != maxIdx1 and (maxIdx2 == -1 or a[j] > a[maxIdx2]):
        maxIdx2 = j
print(a[maxIdx1] * a[maxIdx2])