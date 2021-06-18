def find_multiples(integer, limit):
    times = limit/integer
    lst = []
    count = 1
    while times >= count:
        k = integer*count
        lst.append(k)
        count = count + 1
    return lst
print(find_multiples(5, 25))