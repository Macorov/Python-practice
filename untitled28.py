def is_prime(num):
    
    
    i = 2
    if num == 0 or num == 1 or num < 0 :
        return False
    elif num == 2:
        return True
    elif num > 0 :
        while num > i :
            k = num % i
            if k == 0:
                return False
            i = i + 1
    print("last")
    return True
print(is_prime(29))
    
 