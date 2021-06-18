from itertools import permutations
k = 1234
k = str(k)
l = list(k)
print(l)
lst = []
for num in l:
    num = int(num)
    lst.append(num)
perm = permutations(lst, 4)
for i in list(perm):
    print(i)