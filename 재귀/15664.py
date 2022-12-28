n,m = map(int, input().split())
n_list = list(map(int, input().split()))

result = [0]*10
cnt = [0]*10001

for i in n_list:
    cnt[i] += 1 # 각 숫자가 나온만큼 cnt값으로 

n_list = sorted(list(set(n_list)), reverse=False)

def recursion(n,m,level, be):
    if m==level:
        for i in range(m):
            print(result[i], end=" ")
        print("")
        return
    
    for i in range(len(n_list)):
        if cnt[n_list[i]]!=0 and n_list[i]>=be:
            cnt[n_list[i]]-=1
            result[level] = n_list[i]
            recursion(n,m,level+1, n_list[i])
            cnt[n_list[i]]+=1


recursion(n,m,0,-1)