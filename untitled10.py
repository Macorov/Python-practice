phrase = "hello world"
translation = ""
for letter in phrase:
    if letter in "aeiou":
        if letter in "a":
            translation = translation + "1"
        elif letter in "e":
            translation = translation + "2"
        elif letter in "i":
            translation = translation + "3"
        elif letter in "o":
            translation = translation + "4"
        elif letter in "u":
            translation = translation + "5"
    else:
        translation = translation + letter
print(translation)
            
            
            
            
            