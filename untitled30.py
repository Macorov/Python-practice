def likes(names):
    k = len(names)
    if k == 1:
        n1 = names[0]
        return f"{names[0]} likes this"
    elif k == 2:
        return f"{names[0]} and {names[1]} like this"
    elif k == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif k > 3:
        others = k - 2
        return f"{names[0]}, {names[1]} and {others} others like this"
    elif k == 0:
        return "no one likes this"
print(likes(["Alex", "Jacob", "Mark", "Max", "Jacob", "Mark",]))

        
        


    
    