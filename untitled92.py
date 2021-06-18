def evenator(s):
    
    x = list(s)
    p = ""
    
    lst = [".", ",", "?", "!"]
    f = ""
    for elem in x:
        if elem not in lst:
            p = p + elem
    k = p.split()
    for elem in k:
        if len(elem) % 2 != 0:
            m = elem + elem[-1]
            f = f + m
        else:
            f = f + elem
        f = f + " "
    return f
print(evenator('underscore is not considered a word..in this case,'))