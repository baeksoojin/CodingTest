n,m = map(int, input().split())
n_list = sorted(list(map(int, input().split())),reverse=False)

result = [0]*100
check = [False]*10001

def recursion(n,m, level):
    
    if m==level:
        for i in range(0,m):
            print(result[i], end=" ")
        print("")
        
    for i in range(n):
        if check[i] == False:
            check[i]=True
            result[level] = n_list[i]
            recursion(n,m,level+1)
            check[i]=False


recursion(n,m,0)