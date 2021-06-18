def iq_test(numbers):
    numbers = numbers.split()
    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i])
    even = 0
    odd = 0
    lst1 = []
    lst2 = []
    count = 0

    for num in numbers:
        
        count += 1
        if num % 2 == 0:
            even += 1
            lst1.append(count)
        else:
            odd += 1
            lst2.append(count)
    if even < odd:
        listToStr = ' '.join(map(str, lst1))
        return int(listToStr)
    else:
        listToStr = ' '.join(map(str, lst2))
        return listToStr
print(iq_test("1 2 2"))
    
        

