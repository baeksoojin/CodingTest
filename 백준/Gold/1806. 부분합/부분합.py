'''
부분합이 가장 짧은 것
부분합이 s이하라면 end+1, s이상이라면 

부분합 최소길이
'''

import sys

input = sys.stdin.readline

n,s = map(int, input().split())

nums = list(map(int, input().split()))

start = end = 0

sum = 0
min_len = n
flag = False
while start < n:

    if sum < s: #부분합이 s이하라면 end+1
        if end>=n:
            break
        sum += nums[end]
        end+=1
    else: # 부분합이 s이상이라면 s +1
        flag = True
        min_len = min(min_len, end-start)
        sum -= nums[start]
        start+=1
        

if flag ==False:
    print(0)
else:
    print(min_len)




