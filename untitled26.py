def tickets(people):
    lst = [25, 50, 100]
    c = 0
    
    for money in people:
        
        #print(c)
        fm = money - 25
        if lst == []:
            return "NO"
            print("1")
        elif fm == 0:
            print("2")
            continue
            
        elif fm in lst:
            print("3")
            lst.remove(fm)
        elif fm == 75 and lst[0] + lst[1] == 75 and c == 0:
            c = c + 1
            continue
        else:
            print("4")
            return "NO"
    return "YES"
print(tickets([25, 100]))
            
    