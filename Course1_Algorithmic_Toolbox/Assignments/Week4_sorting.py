# Uses python3
import random

def partition3(a, l, r):
    x = a[l]
    m2 = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            m2 += 1
            a[i], a[m2] = a[m2], a[i]
    a[l], a[m2] = a[m2], a[l]
    m1 = m2
    for i in range(m2-1, l-1, -1):
        if a[i] == x:
            m1 -= 1
            a[i], a[m1] = a[m1], a[i]
    return m1, m2

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def randomized_quick_sort2(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    j = partition2(a, l, r)
    randomized_quick_sort2(a, l, j - 1);
    randomized_quick_sort2(a, j + 1, r);

def randomized_quick_sort3(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort3(a, l, m1 - 1);
    randomized_quick_sort3(a, m2 + 1, r);


n = int(input()) 
a = list(map(int, input().split()))
#a = [123123,112, 232, 11, 232, 11, 232, 11, 23, 11]
n = len(a)
randomized_quick_sort3(a, 0, n - 1)
for x in a:
    print(x, end=' ')
