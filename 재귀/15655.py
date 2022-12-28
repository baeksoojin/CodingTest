n,m = map(int, input().split())
n_list = sorted(list(map(int, input().split())), reverse=False)

result=[0]*100

def recursion(n,m,level, be):
    
    if m==level:
        for i in range(0,m):
            print(result[i], end=" ")
        print("")

    for i in range(n):
        if be<n_list[i]:
            result[level] = n_list[i]
            recursion(n,m,level+1, n_list[i])

recursion(n,m,0,-1)