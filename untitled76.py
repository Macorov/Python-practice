def will_fit(present, box):
    if box == (37,)
    m = list(present)
    k = list(box)
    m.sort()
    k.sort()
    i = 0
    for num in m:
        if num <= k[i] - 1:
            i += 1
        else:
            return False
    return True
print(will_fit((1, 2, 3), (2, 1, 3)))