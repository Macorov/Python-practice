lst = [-3,-2,-1,2,10,15,16,18,19,20]
prev = 0
final = ""
for el in lst:
    if el > prev:
        k = el - prev
        if k < 3:
            k = f"{prev}--{el},"
            final = final + k
        else:
            k = f"{el},"
            