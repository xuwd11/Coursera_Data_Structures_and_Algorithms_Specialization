# Uses python3

def optimal_summands(n):
    summands = []
    #write your code here
    k = n
    l = 1
    while k > 2*l:
        summands.append(l)
        k = k - l
        l = l + 1
    summands.append(k)
    return summands

n = int(input())
summands = optimal_summands(n)
print(len(summands))
for x in summands:
    print(x, end=' ')
