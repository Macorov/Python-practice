def clean_string(s):
    prev = ""
    final = ""
    count = 0
    for el in s:
        if count == 0:
            prev = el
            count += 1
        elif el == "#":
            prev = ""
        else:
            final = final + prev
            prev = el 
    return final
print(clean_string("abc#d##c" ))