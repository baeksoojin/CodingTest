# stack 사용

from collections import deque

n = int(input())
queue = deque([])

dolist = []

for _ in range(n):
    do = list(input().split())
    dolist.append(do)


for i in range(n):
    
    if dolist[i][0] == "push":
        queue.append(int(dolist[i][1]))
    elif dolist[i][0] == "pop":
        if queue:
            print(queue.pop())
        else:
            print("-1")
    elif dolist[i][0] == "size":
        print(len(queue))
    elif dolist[i][0]=="empty":
        if queue:
            print("0")
        else:
            print("1")
    else:
        if queue:
            print(queue[len(queue)-1])
        else:
            print("-1")
