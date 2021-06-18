def all_fibonacci_numbers():
    x,y=0,1
    lst = list()
    while y<= 832040:
        lst.append(y)
        x,y = y,x+y
    return lst
print(all_fibonacci_numbers())