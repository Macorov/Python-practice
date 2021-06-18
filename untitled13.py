def maskify(cc):
    c = list(cc)
    b = len(cc)
    d = b - 4
    count = 0
    if b > 4:
        
        
        while d > count:
            c[count] = "#"
            count += 1
            

            str = ""
            for ele in c:
                str += ele
        return str
    else:
        return cc
    
print(maskify("aa223"))