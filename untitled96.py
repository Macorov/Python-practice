def dup(arry):
    pw = ""
    final = []
    for word in arry:
        count = 0
        for el in word:
            if el == pw:
                word=word.replace(word[count],"")
                
                
            else:
                pw = el
                count += 1
        final.append(word)
    return final
print(dup(["kelless","keenness"]))
                