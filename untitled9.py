matrix = [[], []]
count = 0
sum = 0
  
flatten_matrix = [] 
  
for sublist in matrix: 
    for val in sublist: 
        flatten_matrix.append(val) 
          
while len(flatten_matrix) > count:
    sum = sum + flatten_matrix[count]
    count += 1
print(sum)