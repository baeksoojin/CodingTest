from collections import deque

def solution(arr):
    answer = []
    
    queue = deque(arr)
    before = -1
    
    while(queue):
        first = queue.popleft()
        if first is not before:
            answer.append(first)
            # print(first)
            before = first
    
    return answer