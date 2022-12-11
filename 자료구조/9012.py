# ( -> push, ) -> pop 을 queue나 stack ->deque 사용해서 진행하고 모두 진행됐을 때, 그 길이가 0이여야함.
# pop의 경우에 queue나 stack 길이가 0이 아닐때 진행하도록한다.\
from collections import deque

n = int(input())
checklists = []

for i in range(0,n):
    temp = input()
    checklists.append(temp)

for i in range(0, n):
    stack = deque()
    nullcheck = False
    for j in checklists[i]:
        if j=="(":
            stack.append("(")
        else:
            if len(stack)!=0:
                stack.popleft()
            else:
                nullcheck = True
    if len(stack)==0 and nullcheck == False:
        print("YES")
    else:
        print("NO")

# -> 모두 입력받고 다시 for문을 돌리니까 시간복잡도가 늘어남. -> 입력받고 바로 처리도록 짤 수 있음.
        
                

