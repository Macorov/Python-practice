def count_sheep(n):
    p = 1
    final = ""
    while n >= p :
        q = str(p)
        
        k = f"{q} sheep..."
        
        
        final = final + k
        p += 1
    return final
print(count_sheep(4))
        


        