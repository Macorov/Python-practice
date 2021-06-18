def solve(arr):
    count = 0
    k = len(arr)
    lst = list()
    while count <= k/2:
        print("k")
        p = max(arr)
        q = min(arr)
        lst.append(p)
        lst.append(q)
        arr.remove(max(arr))
        arr.remove(min(arr))
    return lst
print(solve([15,11,10,7,12]))