def solve(n):
    import re
    s = ""
    k = " "
    for letter in n:
        s = s + k + letter
    
    up = re.findall("[A-Z]+",s)
    
    down = re.findall("[a-z]+",s)
    num = re.findall("[0-9]+",s)
    sp = re.findall('[@_!#$%^&*()<>?/\|}{~:]+', s)
    a = len(up)
    b = len(down)
    c = len(num)
    d = len(sp) + 1
    lst = []
    lst.append(a)
    lst.append(b)
    lst.append(c)
    lst.append(d)
    
    return lst
print(solve("RYT'>s&gO-.CM9AKeH?,5317tWGpS<*x2ukXZD"))