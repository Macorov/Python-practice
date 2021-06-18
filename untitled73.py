k = [None, 1, 0, 0, "kamal",False, True]
count = 0
lst = []
for e in k:
    if e is False:
        lst.append(e)
    elif e == 0:
        count += 1
    else:
        print(1)
        lst.append(e)
while count > 0:
    lst.insert(len(lst), 0)
    count = count - 1
print(lst)
