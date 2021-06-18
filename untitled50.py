def halving_sum(n): 
    sum1 = 0
    prev = 0
    count = 2
    while prev != 1:
        if sum1 == 0:
            sum1 = n
        else:
            sum1 = sum1 + n/count
            prev = n/count
            count = count * 2
            
    return sum1
print(halving_sum(25))
            