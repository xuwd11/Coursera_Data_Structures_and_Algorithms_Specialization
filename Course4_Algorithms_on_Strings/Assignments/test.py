#python3

class A:
    total = 0
    def __init__(self):
        A.total += 1
        self.id = self.total - 1

b = A()
c = A()
print(b.id, c.id)
