import itertools

def solution(nums):
    answer = 0
    
    max_size = len(nums)//2
    type = set(nums)
    
    if len(type) >=max_size:
        answer = max_size
    else:
        answer = len(type)

    
    return answer