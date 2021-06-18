def anagrams(word, words):
    lst = list(word)
    lst.sort()
    final = list()
    for element in words:
        k = list(element)
        k.sort()
        if k == lst:
            final.append(element)
    return final
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))