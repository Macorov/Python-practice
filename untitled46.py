def duplicate_count(text):
    counts = dict()
    final = dict()
    

    words = list(text)
    
    for word in words:
          counts[word] = counts.get(word, 0) + 1
          
    k = counts.items()
    lst = list(k)
    return lst
print(duplicate_count("abracadabra"))