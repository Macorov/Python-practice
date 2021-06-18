import math
count = 0
sum = 0
b = isinstance(count,int)
solve = 12
while solve > count:
    sum = solve + count
    k = math.sqrt(sum)
    if isinstance(k,int) == True:
        print(count)
        break
    else:
        continue
print(count)