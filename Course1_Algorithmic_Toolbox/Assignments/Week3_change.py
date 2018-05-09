# Uses python3

def get_change():
    #write your code here
    m = int(input())
    n = int(m/10) + int((m%10)/5) + (m%10)%5
    return n

print(get_change())
