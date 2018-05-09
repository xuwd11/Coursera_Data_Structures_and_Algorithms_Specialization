# Uses python3

'''
def MergeSort(a, b, left, right):
    if right - left < 2:
        return
    mid = (left+right)//2
    MergeSort(a,b,left,mid)
    MergeSort(a,b,mid,right)
    Merge(a,b,left,mid,right)
    a[left:right] = b[left:right]

def Merge(a, b, left, mid, right):
    i = left
    j = mid
    for k in range(left, right):
        if (i < mid) and ((j >= right) or (a[i] <= a[j])):
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
'''

def get_ni(a, left, right):
    if right - left < 2:
        return(a[left:right], 0)
    mid = (left+right)//2
    b, ni1 = get_ni(a, left, mid)
    c, ni2 = get_ni(a, mid, right)
    a1, ni3 = get_ni_merge(b, c)
    ni = ni1 + ni2 + ni3
    return(a1, ni)

def get_ni_merge(b, c):
    d = []
    ni = 0
    while b and c:
        if b[0] <= c[0]:
            d.append(b.pop(0))
        else:
            ni += len(b)
            d.append(c.pop(0))
    while b:
        d.append(b.pop(0))
    while c:
        d.append(c.pop(0))
    return(d, ni)


n = input() 
a = list(map(int, input().split()))
b = len(a)*[0]
ni = get_ni(a,0,len(a))[1]
print(ni)