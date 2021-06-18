def is_square(n):
    if n < 0:
        return False
    elif n == 0 :
        return True 
    
    m = int(n**0.5)
    if m**2 == int(n):
        return True
    else:
        return False