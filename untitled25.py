a = [1, 1, 2, 3, 5, 6, 7]

ind2remove = [1, 3]

for numbers in a:
    
    for i in sorted(ind2remove, reverse=True):
        del a[i]
        
        


print(a)