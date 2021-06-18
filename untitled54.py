def alphabet_position(text):
    import string
    alphanumeric_filter = filter(str.isalnum, text)
    tt = "".join(alphanumeric_filter)
    m = tt.lower()
    k = list(m)
    lst = list()
    for char in k:
        k = string.ascii_lowercase.index(char) + 1
        lst.append(k)
    stringList = ' '.join([str(item) for item in lst ])
    return stringList
print(alphabet_position("The sunset sets at twelve o clock"))