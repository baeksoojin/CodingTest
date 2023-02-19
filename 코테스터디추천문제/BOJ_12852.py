'''
전형적인 dp
연산 횟수의 최솟값을 앞의 수부터 담아가면서 체크

1일때를 체크하지 않아서 100%때 런타임에러남 -> 1일때는 0번횟수반복 1만 출력

'''

n = int(input())

result = [0]*(10**6+1)



result[2] = (1,1)
result[3] = (1,1)
INF = 1e9

for i in range(4,n+1):

    a=b=c=INF
    
    a = result[i-1][0]+1
    if i%3==0:
        b = result[i//3][0]+1
    if i%2==0:
        c = result[i//2][0]+1

    min_temp = min(a,b,c)
    if  min_temp == a:
        result[i] = (a,i-1)
    elif min_temp == b:
        result[i] = (b,i//3)
    else:
        result[i] = (c,i//2)
   
if n==1:
    print("0")
    print("1")
else:

    print(result[n][0])
    temp=result[n][1]
    print(n, end=" ")
    while(True):
        print(temp, end=" ")
        if temp==1:
            break
        temp = result[temp][1]
    print()
