a = [1,2,2,2,3]
b = [2]
final = list()
for number in a:
    if number not in b:
        
        final.append(number)
print(final)
    