def isPP(n):
    k = n/2
    a = 2
    p = 2
    test = 0
    final = list()
    while a < n:
        while test <= n:
            test = pow(a, p)
            if test == n:
                return [a,p]
            if a < k:
                a += 1
            else:
                p += 1
        return None
print(isPP(9))