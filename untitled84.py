def reverse_alternate(string):
    k = string.split()
    lst = []
    count = 1
    for word in k:
        if count % 2 == 0:
            f = word[::-1]
            lst.append(f)
            count += 1
        else:
            lst.append(word)
            count += 1
    final = ' '.join(str(i) for i in lst)
    return final
print(reverse_alternate("Have a beer"))