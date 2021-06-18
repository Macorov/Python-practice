def format_words(wordk):
    words = []
    if wordk == None:
        return ""
    for word in wordk:
        
        if word != "":
            words.append(word)
    
    fcount = len(words)
    count = 0
    final = ""
    if len(words) == 1:
        return words[0]
    while count < fcount:
        if count + 1 == fcount:
            final = final + "and" + " " + words[count]
        elif count + 2 == fcount:
            final = final + words[count] + " "
            
        else:
            final = final + words[count] + "," + " "
        count += 1
    
    return final
print(format_words(['one', 'two', 'three', 'four']))