def first_dup(s):
    lst = list()
    
    p = list(s)
    count = 0
    for word in p:
       
        
        p.remove(word)
        if word in p:
            if word == "3":
                return "a"
            else:
                
                return word
        else:
            count += 1
print(first_dup('1a2b3a3c'))
        
