import sys
n = int(input())

plan = sys.stdin.readline().strip().split(" ")

i,j = (1,1)

for t in range(len(plan)):
    if plan[t]=="D" and i<=n:
        i = i+1
    if plan[t]=="U" and i-1>=1:
        i = i-1
    if plan[t]=="L" and j-1>=1:
        j = j-1
    if plan[t]=="R" and j<=n:
        j = j+1
print(i,j)

        