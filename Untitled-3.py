def get_order(k):
    f = ["milkshake", "fries", "chicken", "pizza", "sandwich", "onionrings", "milkshake", "coke", "burger"]
    m = len(k)
    lst = []
    count = 0
    pcount = 0
    while count <= m:
        l = k[pcount:count] 
    
        if l in f:
            l = l.capitalize()
            pcount = count
            lst.append(l)
        count += 1
    final = ""
    count = 0
    k = lst.count("Burger")

    while count < k:
        final = final + "Burger" + " "
        count += 1
    count = 0
    k = lst.count("Fries")
    while count < k:
        final = final + "Fries" + " "
        count += 1
    count = 0
    k = lst.count("Chicken")
    while count < k:
        final = final + "Chicken" + " "
        count += 1
    count = 0
    k = lst.count("Pizza")
    while count < k:
        final = final + "Pizza" + " "
        count += 1
    count = 0
    k = lst.count("Sandwich")
    while count < k:
        final = final + "Sandwich" + " "
        count += 1
    count = 0
    k = lst.count("Onionrings")
    while count < k:
        final = final + "Onionrings" + " "
        count += 1
    count = 0
    k = lst.count("Milkshake")
    while count < k:
        final = final + "Milkshake" + " "
        count += 1
    count = 0
    k = lst.count("Coke")
    while count < k:
        final = final + "Coke" + " "
        count += 1
    final = final.strip()
    return final
