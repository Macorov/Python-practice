def solution(nums=[]):
    if nums == [] or nums == None:
        return []
    nums.sort()
    return nums
    
print(solution(None))