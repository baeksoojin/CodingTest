'''
제거한 위치 바로 직전 위치에서 검토 재시작
'''
from collections import deque
import copy
def solution(s):

    if len(s)%2 == 1: # 홀수개인 경우
        return 0
    
    stack = deque(s[0])
    
    #print(stack.pop()) # 마지막꺼 꺼냄
    #print(stack[-1])# 마지막꺼 꺼냄
    
    for i in range(1,len(s)):
        
        if len(stack)==0:
            stack.append(s[i])
            continue
        if stack[-1] == s[i]: # stack에서 빼내기
            stack.pop()
        else: # stack에 넣기
            stack.append(s[i])
    if stack:
        return 0
    else:
        return 1