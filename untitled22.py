name = "Mahfuz Mukto Jr  f"
k =""
count = 0
m = "."
for word in name.split():
    if count == 0:
        k = word[0]
        count = count + 1
    elif count > 0:
        k = k + m + word[0]
 final = k.upper()
print(final)
    