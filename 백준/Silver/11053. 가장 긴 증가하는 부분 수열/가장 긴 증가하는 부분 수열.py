#가장 긴 증가하는 수열

n = int(input())
list1 = []#입력받은 수
array = [0]*(n+1)#개수 저장
list2=[]
list2 = list(map(int,input().split()))
list1.append(-1)#list[0]=0
list1.extend(list2)#list[1]부터 입력값을 담기위해 list병합

#print(list1)
array[0]=0

for j in range(1,n+1):
    m = -1
    for h in range(0, j):
        if(list1[h] < list1[j] and m<=array[h]):
            array[j]=array[h]+1
            m = array[h]

temp =0
for i in range(1,n+1):
    if(temp<array[i]):
        temp = array[i]

print(temp)

