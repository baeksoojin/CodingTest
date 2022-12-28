#순열 ->다만 같은 숫자가 입력될 수 있고 이때 값이 중복되면 안 되니까 cnt로 중복 체크해줘야함

n,m = map(int, input().split())
n_list = list(map(int, input().split()))

cnt = [m-1]*10001
for i in n_list:
    cnt[i]+=1

n_list = sorted(list(set(n_list)),reverse=False)

result = [0]*10

def recursion(n,m,level):

    if m==level:
        for i in range(m):
            print(result[i], end=" ")
        print("")
        return

    for i in range(len(n_list)):
        if cnt[n_list[i]]!=0:
            cnt[n_list[i]]-=1
            result[level] = n_list[i]
            recursion(n,m,level+1)
            cnt[n_list[i]]+=1

recursion(n,m,0)