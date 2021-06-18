def test_it(a, b):
    a = str(a)
    b = str(b)
    if len(a) > 1:
        a = a.strip("0")
    if len(b) > 1:
        b = b.strip("0")
    k = int(a)
    l = int(b)
    final = k * l
    return final 
print(test_it(5000000, 6))