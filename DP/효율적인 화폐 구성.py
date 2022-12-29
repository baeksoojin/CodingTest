#6시 15분 시작 -> 45분까지 목표
# 42분 풀기완료 

n,m = map(int, input().split())

result = [99999]*10001

n_list = []
for i in range(n):
    n_list.append(int(input()))
    result[n_list[i]] = 1
#화폐 단위 입력받기

result[0] = 0
for i in range(1,m+1):
    for j in range(0,(i+1)//2+1):
        if result[j]!=99999:
            result[i] = min(result[i], result[j] + result[i-j])
print(result)
if result[m]==99999:
    print("-1")
else:
    print(result[m])
