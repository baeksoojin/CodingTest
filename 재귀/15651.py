n,m = map(int, input().split())

result = [0]*100

def recursion(n,m,level):
    
    if m==level:
        for i in range(m):
            print(result[i],end=" ")
        print("")
        return

    for i in range(1,n+1):
        result[level] = i
        recursion(n,m,level+1)

recursion(n,m,0)