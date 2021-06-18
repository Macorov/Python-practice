def scramble(s1, s2):
    k = list(s1)
    for letter in s2:
        if letter in k:
            k.remove(letter)
        else:
            return False
    return True
print(scramble('katas', 'steak'))