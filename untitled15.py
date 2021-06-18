def high_and_low(numbers):
    lst = list(numbers)
    lst = [elt.strip() if type(elt) is str else elt for elt in lst]
    while '' in lst:
        
        lst.remove('')
        
    
   
    p = max(lst)
    q = min(lst)
    final = str(p) + " " + str(q)
    
    return lst
print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))