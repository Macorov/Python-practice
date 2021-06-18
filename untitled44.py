def remove(p):
    if p == "":
        return False
    if len(p) > 140:
        return False
    s = p.lower()
    lst = [word[0].upper() + word[1:] for word in s.split()]
    s = " ".join(lst)
    
    k = s.replace(" ", "")
    return f"#{k}"
      
# Driver Program 
string = 'codeWars is nice'

print(remove(string)) 