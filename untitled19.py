word = "ultrarevolutionariees"
count = 0
vowels = "aeiou"
lst = list(word)
time = len(lst)
high = None

for ch in word:
    if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
        if high == None:
            high = ch
            count += 1
        elif ch == high :
            count += 1
            high = ch
        
        
    
        
    
    
    
  