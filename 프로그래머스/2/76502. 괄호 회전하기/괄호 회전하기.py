'''
12시 47분 시작

1. 스택 사용해서 올바른지 체크하는 함수
2. x만큼 회전하는 함수

'''

from collections import deque

def find_pair(c):
    if c=="}":
        return "{"
    elif c==")":
        return "("
    else:
        return "["

def is_correct(s):
    stack = deque()
    
    for i in range(len(s)):
        if i==0 or s[i]=="(" or s[i] =="{" or s[i] =="[":
            if i==0 and not(s[i]=="(" or s[i] =="{" or s[i] =="["):
                return False
            stack.append(s[i])
        else:
            if len(stack)==0:
                return False
            temp = stack.pop()
            if temp != find_pair(s[i]):
                return False
    
    if len(stack)==0:
        
        return True
    else:
        return False
    
    

def solution(s):
    answer = 0
    
    if len(s)==1: # 1일때는 무조건 불가능
        return answer
    
    for i in range(len(s)):
        
        if i!=0: # 0 일때는 그대로
            s = s[1:] + s[0]
        if is_correct(s):
            answer+=1
    
    
    return answer