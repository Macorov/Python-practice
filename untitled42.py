def check_exam(arr1,arr2):
    count = 0
    answer = 0
    while count <= len(arr1):
        if arr2[count] == "":
            
            continue
        
        elif arr1[count] == arr2[count]:
            
            print("k")
            answer = answer + 4
        elif arr1 != arr2:
            answer = answer - 1
        count = count + 1
    return answer
print(check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]))
            