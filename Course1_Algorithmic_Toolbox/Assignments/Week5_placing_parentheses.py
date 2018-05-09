# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinAndMax(_min_, _max_, i, j, op):
    _min = float('inf')
    _max = float('-inf')
    for  k in range(i, j):
        a = evalt(_max_[i][k], _max_[k+1][j], op[k])
        b = evalt(_max_[i][k], _min_[k+1][j], op[k])
        c = evalt(_min_[i][k], _max_[k+1][j], op[k])
        d = evalt(_min_[i][k], _min_[k+1][j], op[k])
        _min = min([_min, a, b, c, d])
        _max = max([_max, a, b, c, d])
        #print(a, b, c, d)
    #print(_min,_max)
    return _min, _max

def get_maximum_value(dataset):
    #write your code here
    d = dataset[::2]
    d = list(map(int, d))
    op = dataset[1::2]
    n = len(d)
    _min_ = [([0]*n) for row in range(n)]
    _max_ = [([0]*n) for row in range(n)]
    for i in range(n):
        _min_[i][i] = d[i]
        _max_[i][i] = d[i]
    for s in range(1, n):
        for i in range(n-s):
            j = i+s
            _min = float('inf')
            _max = float('-inf')
            for  k in range(i, j):
                a = evalt(_max_[i][k], _max_[k+1][j], op[k])
                b = evalt(_max_[i][k], _min_[k+1][j], op[k])
                c = evalt(_min_[i][k], _max_[k+1][j], op[k])
                d = evalt(_min_[i][k], _min_[k+1][j], op[k])
                _min = min([_min, a, b, c, d])
                _max = max([_max, a, b, c, d])
                #print(i,k,j,a,b,c,d,_min,_max)
            _min_[i][j] = _min
            _max_[i][j] = _max
            #print(i, j, _min, _min_[i][j],_max, _max_[i][j])            
    return _max_[0][n-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
