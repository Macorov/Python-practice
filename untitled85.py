def test_it(a, b):
    a = str(a)
    b = str(b)
    a = list(a)
    b = list(b)
    k = [int(i) for i in a]
    l = [int(i) for i in b]
    i = len(k)
    lst =[]
    count = 0
    while count < i:
        if k[count] != 0:
            lst.append()
            count += 1
    
    return k
print(test_it(30000,3))