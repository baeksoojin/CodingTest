import sys
input = sys.stdin.readline

n,m = map(int, input().split())

list1 ={}
list2 =[]


for i in range(n):
    list1[input().strip()]=i
for i in range(m):
    temp = input().strip()
    if temp in list1.keys():
        list2.append(temp)

list2.sort()
print(len(list2))
for i in list2:
    print(i)