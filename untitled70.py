def spin_words(sentence):
    k = sentence.split()
    count = 1
    final = ""
    if len(k) == 1 and len(sentence) >= 5:
        return sentence[::-1]
    if len(k) == 1:
        return sentence
    for word in k:
        if len(word) >= 5:
            txt = word[::-1]
            if count ==  1:
                final = txt
                count += 1
            else:
                final = final + " " + txt
        else:
            if count == 1:
                final = word
                count += 1
            else:
                final = final + " " + word
    return final
print(spin_words("Hey fellow warriors"))

