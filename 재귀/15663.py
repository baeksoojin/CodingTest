# cnt값을 두고 0이 아닐때까지 돌기

n,m = map(int, input().split())
n_list = list(map(int, input().split()))

cnt=[0]*10001

for i in n_list:
    cnt[i] += 1

result = [0]*10
n_list = sorted(list(set(n_list)), reverse=False)

def recursion(n,m,level):

    if m==level:
        for i in range(m):
            print(result[i], end=" ")
        print("")
        return
    
    for i in range(len(n_list)):
        if cnt[n_list[i]]:
            cnt[n_list[i]] -= 1
            result[level] = n_list[i]
            recursion(n,m,level+1)
            cnt[n_list[i]] += 1

recursion(n,m,0)
