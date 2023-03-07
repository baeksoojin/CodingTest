'''
for문을 돌리면 되지 않을까?

최소공배수까지가 마지막수이니까 그때까지 수를 돌면되는데 다 돌면 비효율적이니까
특정수를 M으로 나눈 나머지가 x인 것이니, []%M==x를 만족하는 수일때만 y값을 체크

'''

import math

N = int(input())
for i in range(N):
    m,n,x,y = map(int, input().split())
    result = -1

    for i in range(x,n*m+1,m):
        
        if (i - y) % n ==0:
            result = i
            break
    print(result)