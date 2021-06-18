def num_key_strokes(text):
    count = 0
    lst = [";", ",", ".", "/", "=", "-"]
    text = list(text)
    
    for ch in text:
        
        if ch.isdigit():
            
            count += 1
        elif(ch.isalpha()):
            if ch.isupper():
                
                count += 2
            else:
                count += 1
        elif ch == " ":
            
            count += 1
        elif ch in lst:
            count += 1
        else :
            count += 2
    return count
print(num_key_strokes("This is a long SEnteNce.1"))
