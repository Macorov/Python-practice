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
        if words[count] == words[-1]:
            final = final + "and" + " " + words[count]
        elif words[count + 1] == words[-1]:
            final = final + words[count] + " "
            
        else:
            final = final + words[count] + "," + " "
        count += 1
    
    return final
print(format_words(['one']))