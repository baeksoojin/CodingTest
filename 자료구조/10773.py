# 0 일때 가장 최근 수를 지움 -> 0일때 stack에서 pop
# 모든 과정 끝에 stack에 남은 수를 모두 더함 -> sum(list)

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

num_list = []

for i in range(n):
    num_list.append(int(input()))

queue = deque([])

for num in num_list:
    
    if num == 0:
        queue.pop()
    else:
        queue.append(num)
    
print(sum(queue))
