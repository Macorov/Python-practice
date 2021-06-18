def get_middle(txt):
    m = len(txt)-1
    k = m//2
    a = len(txt)+2
    b = a//2
    final = txt[k:b]
    return final
print(get_middle("banan"))