def validate_pin(pin):
    import ast
    p = len(pin)
    
    if p == 4 or p == 6:
        try:
            #k = ast.literal_eval(pin)
            k = int(pin)
            if type(k) == int:
                return True
            else:
                return False
        except:
            return False
    else:
        return False
print(validate_pin("24444"))