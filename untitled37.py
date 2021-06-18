def square_digits(num):
    digits = [int(x) for x in str(num)]
    lst = []
    for num in digits:
        k = num*num
        lst.append(k)
    listToStr = ''.join([str(elem) for elem in lst]) 
    final = int(listToStr)
    return final
print(square_digits(9119))


    