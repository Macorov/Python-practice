def duplicate_count(text):
    counts = dict()
    final = dict()
    

    words = list(text)
    print(words)
    for word in words:
          counts[word] = counts.get(word, 0) + 1


    for word,value in counts.items():
        
        
        
        final[word] = value
    return final
print(duplicate_count("abbbaacde"))    