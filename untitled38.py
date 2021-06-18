def scramble(s1, s2):
    k = list(s1)
    p = list(s2)
    k = list(dict.fromkeys(k))
    p = list(dict.fromkeys(p))
    for letter in p:
        if letter in k:
            k.remove(letter)
        else:
            return False
    return True
print(scramble("hcjewdjzwpraiezq",  "zhedjaqzrcejpiww"))