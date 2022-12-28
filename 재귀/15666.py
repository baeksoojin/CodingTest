n,m = map(int, input().split())
n_list = list(map(int, input().split()))

cnt = [m-1]*10001
for i in n_list:
    cnt[i]+=1

n_list = sorted(list(set(n_list)),reverse=False)
result = [0]*10

def recursion(n,m,level,be):# 이전의 수보다 크거나 같아야함

    if m==level:
        for i in range(m):
            print(result[i], end=" ")
        print()
        return
    
    for i in range(len(n_list)):
        if be <= n_list[i] and cnt[n_list[i]]!=0:
            cnt[n_list[i]]-=1
            result[level] = n_list[i]
            recursion(n,m,level+1, n_list[i])
            cnt[n_list[i]]+=1
        
recursion(n,m,0,-1)