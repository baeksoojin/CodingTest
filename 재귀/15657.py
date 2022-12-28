# 전 레벨보다 크거나 같은 수만 출력 가능.
n,m = map(int, input().split())
n_list = sorted(list(map(int, input().split())),reverse=False)

result = [0]*10

def recursion(n,m,level, be):
    
    if m==level:
        for i in range(m):
            print(result[i], end=" ")
        print("")
        return
    
    for i in range(n):
        if be<=n_list[i]:
            result[level] = n_list[i]
            recursion(n,m,level+1,n_list[i])

recursion(n,m,0,-1)