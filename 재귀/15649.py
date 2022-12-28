n,m = map(int,input().split())

result =[0]*100
check = [False]*10

def recursion(n,m, level):
    
    if level==m:
        for i in range(m):
            print(result[i], end=" ")
        print("")
    
    for i in range(1,n+1):
        if check[i]==False:
            result[level] = i
            check[i]=True
            recursion(n,m,level+1)
            check[i]=False

recursion(n,m,0)