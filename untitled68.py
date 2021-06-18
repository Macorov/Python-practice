def find_it(seq):
    from collections import Counter
    occ = Counter(seq)
    for num,val in occ.items():
        if val % 2 != 0:
            return num
print(find_it([10]))
            