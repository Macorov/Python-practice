def largest_pair_sum(numbers):
    lst = numbers
    oldsum = 0
    newsum = 0
    count = 1
    for num in numbers:
        while len(lst) >= count:
            newsum = num + lst[count]
            if newsum > oldsum:
                oldsum = newsum
                count = count + 1
        lst.remove(num)
    return oldsum
print(largest_pair_sum([10, 14, 2, 23, 19]))
            
            
            
        
    