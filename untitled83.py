def name_in_str(sen, name):
    name = name.lower()
    sen = sen.lower()
    name =  list(name)
    lst = list(sen)
    for word in name:
        if word in lst:
            x = lst.index(word) + 1
            del lst[0:x]
        else:
            return False
    return True 

print(name_in_str("thomas","Thomas"))