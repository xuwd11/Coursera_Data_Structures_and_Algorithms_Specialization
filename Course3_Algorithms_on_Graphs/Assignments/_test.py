# python3

a = 100
def aaa():
    #global a
    a = 10
    bbb()
def bbb():
    global a
    a += 10

aaa()
print(a)