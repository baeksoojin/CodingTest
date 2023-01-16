'''

한칸 혹은 두칸만 이동이 가능하고
연속된 세개의 계단을 모두 밝으면 안 됨(한칸씩 3번 가는 경우가 안 됨) -> 1칸 전으로 이동할 경우 그 2칸 전과 더해줘야함!

- 계단 위치를 for문으로 돌면서 이전 계단과 2칸 이전의 계단중 큰 값을 선택함
다만 여기서 중요한 것은 이전 계단을 선택한 경우 한번만 더 이전계단을 선택할 수 있고 또 이전계단을 선택할 수 없음.
따라서 이전계단을 선택하고 2칸 이전에 담긴 update된 result값(2칸 이전 계단에서의 max값)을 사용해야함.

'''

import sys
input = sys.stdin.readline

n = int(input())

n_list =[]
n_list.append(0)
for i in range(n):
    n_list.append(int(input()))

result=[0]*(n+1)
result[0] = 0
result[1] = n_list[1]
result[2] = n_list[1]+n_list[2]

for i in range(3,n+1):
    result[i] = max(n_list[i-1]+result[i-3], result[i-2] )+ n_list[i]
    print( result,max(n_list[i-1]+result[i-3], result[i-2]), i,result[i])
print(result[n])