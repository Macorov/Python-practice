def duplicate_count(text):
    counts = dict()

    words = list(text)
    print(words)
    for word in words:
         counts[word] = counts.get(word, 0) + 1
    bigword = None
    bigcount = None
    for word,count in counts.items():
        if bigcount is None or count > bigcount:
            bigword = word
            bigcount = count
    return bigword,bigcount
    #print(bigword,bigcount)
x = duplicate_count("abcda")
print(x)