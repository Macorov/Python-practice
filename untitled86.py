def create_phone_number(n):
    lst1 = []
    lst2 = []
    lst3 = []
    count = 0
    for num in n:
        if count < 3:
            lst1.append(num)
        elif count < 6:
            lst2.append(num)
        else:
            lst3.append(num)
        count += 1
    k = ''.join(str(i) for i in lst1)
    l = ''.join(str(i) for i in lst2)
    m = ''.join(str(i) for i in lst3)
    final = f"({k}) {l}-{m}"
    return final
    
print(create_phone_number([0, 3, 0, 0, 0, 0, 0, 0, 0, 0]))
    