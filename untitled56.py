def solution(a, b):
    if type(a) == str :
        if len(a) > len(b):
            final = b + a + b
            return final
        else:
            final = a + b + a
            return final
    k = str(a)
    l = str(b)
    if a > b :
        final = l + k + l
    elif b > a:
        final = k + l + k
    return str(final)
print(solution("U","false"))