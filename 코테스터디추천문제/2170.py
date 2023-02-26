'''

아이디어)
start,end를 바꿔가면서 end보다 start값이 커지는 시점에 end-start를 sum에 더하기?

'''

import sys
input=sys.stdin.readline

n = int(input())

lines =[]

for i in range(n):
    a,b = map(int, input().split())
    lines.append((a,b))


lines.sort()

start=lines[0][0]
end = lines[0][1]

f_start  = start
f_end = l_end = end
# print(start,end)
sum=0
flag=False
for i in range(1,len(lines)):
    # print(start,end)
    if end<lines[i][0]:
        sum += end-start
        # print("sum",sum)
        l_end = end
        # print("change start, end")
        start = lines[i][0]
        end = lines[i][1]
        flag = True
    else:
        if lines[i][1] > end:
            end = lines[i][1] 
        flag=False
if flag==True or(flag==False and l_end!=end) or (flag==False and f_start==start and f_end==end):
    # print(start,end)
    sum+=end-start


print(sum)

    
    


