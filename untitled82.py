def test_it(a, b):
    a = str(a)
    b = str(b)
    a = list(a)
    b = list(b)
    
    lst1 = []
    lst2 = []
    for num in a:
      
        if num != "0":
            lst1.append(num)
    for num in b:
        if num != "0":
            lst2.append(num)
    
    k = [int(i) for i in lst1]
    l = [int(i) for i in lst2]
    k = int(''.join(str(i) for i in k))
    l = int(''.join(str(i) for i in l))
    return k*l
print(test_it(5005, 9))