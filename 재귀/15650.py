from re import I


n,m= map(int,input().split())

check = [False]*100
result=[0]*100

def recursion(n,m,level,before):

    if m==level:
        for i in range(m):
            print(result[i], end=" ")
        print("")
    
    for i in range(1,n+1):
        if check[i]==False and i>before:
            result[level] = i
            check[i]=True
            recursion(n,m,level+1, i)
            check[i]=False

before = -1
recursion(n,m,0,before)