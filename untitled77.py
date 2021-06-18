def comp(array1, array2):
    for num in array1:
        if num*num not in array2:
            return False
    return True 
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]))