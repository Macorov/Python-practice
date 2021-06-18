def rankings(arr):
    m = sorted(arr)
    k = m[::-1]
    final = []
    for num in arr:
        i = k.index(num) + 1
        final.append(i)
    return final
print(rankings([10,20,40,50,30]))