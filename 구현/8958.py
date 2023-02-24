'''
5시54분 시작

'''

import sys

input = sys.stdin.readline

n = int(input())

def oxquiz(t):

    total = 0
    sum = 1
    for i in t:
        if(i=="X"):
            sum = 1
        else:
            total += sum
            sum+=1
        
    print(total)

for _ in range(n):
    test_case = input().rstrip()
    oxquiz(test_case)
    
    


