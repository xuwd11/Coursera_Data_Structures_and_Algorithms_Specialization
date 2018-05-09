# Uses python3

def binary_search(a, x):
    left, right = 0, len(a) - 1
    # write your code here
    while left <= right:
        mid = int((left+right)/2)
        if a[mid] == x:
            return mid
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

data1 = list(map(int, input().split()))
n = data1[0]
a = data1[1 : n + 1]
data2 = list(map(int, input().split()))
m = data2[1 : len(data2)+1]
for x in m:
    # replace with the call to binary_search when implemented
    print(binary_search(a, x), end = ' ')
