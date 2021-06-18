def order(lst):
    numbers = []
    k = lst.split()
    m = list(lst)
    for word in m:
        if word.isdigit():
            numbers.append(int(word))
    for i in range(len(numbers)):
        numbers[i] = numbers[i] - 1
    k = [k[i] for i in numbers]
    return k
print(order("4of Fo1r pe6ople g3ood th5e the2"))