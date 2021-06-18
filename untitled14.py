str = "hello world"
phrase = str.split()
print(phrase)
count = 0
i = len(phrase)
for word in phrase:
    
    print(word)
    k = list(word)
    p = len(word)
    a = word[1]
    b = word[0]
    if count==0:
       # word[0] = ord(b)
        print(word[0])
    elif count==1:
        #word[1] = word[p]
        #word[p] = a
    count = count + 1
    
print(phrase)
    
        
        
        
