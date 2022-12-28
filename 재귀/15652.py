# 레벨이 깊어지면서 선택되는 수가 전의 수보다 작으면 안 되도록 재귀
n,m = map(int, input().split())

result=[0]*100

def recursion(n,m,level, before):
    
    if m==level:
        for i in range(m):
            print(result[i], end=" ")
        print("")
        return
    
    for i in range(1,n+1):
        if i>=before:
            result[level] = i
            recursion(n,m,level+1, i)
    
recursion(n,m,0,-1)
