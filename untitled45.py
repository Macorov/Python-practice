def all_fibonacci_numbers(nterms):
    n1 = 0
    n2 = 1
    count = 1
    lst = list()
    while count < nterms:
        
        nth = n1 + n2
        n1 = n2
        n2 = nth
        lst.append(nth)
        count = count + 1
    return lst
print(all_fibonacci_numbers(30))