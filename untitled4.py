counts = dict()
final = dict()
text = "abcdagggopp"

words = list(text)
print(words)
for word in words:
      counts[word] = counts.get(word, 0) + 1
print(counts)

for word,value in counts.items():
    if value > 1:
        final[word] = value
print(final)
    
        
        
        
    
         