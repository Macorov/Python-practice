def string_letter_count(text):
    
    counts = dict()
    final = dict()
    h = ""

    words = list(text)
    print(words)
    for word in words:
        
        counts[word] = counts.get(word, 0) + 1
    for word,value in counts.item():
        h = h + value + word
    return h
print(string_letter_count("This is a test sentence." ))