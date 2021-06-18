lst = "4of Fo1r pe6ople g3ood th5e the2"
numbers = []
k = lst.split()
m = list(lst)
for word in m:
    if word.isdigit():
        numbers.append(int(word))
print(numbers)
for i in range(len(numbers)):
    numbers[i] = numbers[i] - 1
print(numbers)
k = [k[i] for i in numbers]
print(k)
