def capitalize(s,ind):
    
    
    word = list(s)
    
    for num in ind:
        if num + 1 > len(s):
            break
            
        word[num] = word[num].upper()
    str1 = ""            
    for ele in word:
    
    
        str1 += ele
    return str1
print(capitalize("abcdef",[1,2,5,100]))
    
        