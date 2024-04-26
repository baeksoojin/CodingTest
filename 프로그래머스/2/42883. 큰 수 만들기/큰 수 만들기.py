from collections import deque


def solution(number, k):
    answer = ''
    
    # stack을 사용해서 가장 큰 수를 생성
    
    stack = deque()
    
    pop_count = 0
    
    for i in range(len(number)):
        
        while len(stack) >0 and stack[-1] < number[i] and pop_count <k:
            stack.pop()
            pop_count+=1
        
        if len(stack) < len(number) -k:
            stack.append(number[i])
    
    return ''.join(stack)