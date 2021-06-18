def duplicate_count(text):
    counts = dict()
    
    counting = 0
    
    p = text.lower()
    words = list(p)
    
    for word in words:
          counts[word] = counts.get(word, 0) + 1


    for word,value in counts.items():
        if value > 1:
           counting = counting + 1
    return counting
print(duplicate_count("aabBcde11"))    

