import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
do_list = []
for _ in range(n):
    do_list.append(list(input().split()))

queue = deque([])

for i in range(n):

    if do_list[i][0] == "push":
        queue.append(do_list[i][1])
    elif do_list[i][0] == "front":
        if queue:
            print(queue[0])
        else:
            print("-1")
    elif do_list[i][0] == "back":
        if queue:
            print(queue[len(queue)-1])
        else:
            print("-1")
    elif do_list[i][0] == "size":
        print(len(queue))
    elif do_list[i][0] == "empty":
        if queue:
            print("0")
        else:
            print("1")
    else: #pop
        if queue:
            print(queue.popleft())
        else:
            print("-1")
        
 
    