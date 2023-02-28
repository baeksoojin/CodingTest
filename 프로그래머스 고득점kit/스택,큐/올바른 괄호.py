from collections import deque

def solution(s):
    answer = True
    
    queue = deque(s)
    stack = deque([])
    # (를 넣고 )가 나오면 빼고 다 했는데 s에 남아있거나 중간에 '('가 없는데 빼려고 했다면 false
    
    while(queue):
        
        temp = queue.popleft()
        
        if temp=='(':
            stack.append(temp)
        else:
            if stack:
                stack.pop()
            else:
                return False
            
    if stack:
        return False
    return True