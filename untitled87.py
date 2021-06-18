import string
text = "magi-got-ma-bankacc"
text = [x.replace('-', ' ') for x in text]
k = ''.join(str(i) for i in text)
k = k.split()
f = []
for word in k:
    i = word.capitalize()
    f.append(i)
final = ' '.join(str(i) for i in f)
print(final)
    