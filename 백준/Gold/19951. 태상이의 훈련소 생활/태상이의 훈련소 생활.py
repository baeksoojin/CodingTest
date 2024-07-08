import sys
input = sys.stdin.readline

n,m= map(int, input().split())

n_list = list(map(int, input().split()))
n_list = [0] + n_list

change_flag = [0]*(len(n_list)+1)

for i in range(m):
    a,b,h = map(int, input().split())
    change_flag[a] += h
    change_flag[b+1] -= h
sum = [0]*(n+1)
for i in range(1,n+1):
    sum[i] = sum[i-1] + change_flag[i]
for i in range(1, n+1):

    n_list[i] += sum[i]
    print(n_list[i], end= " ")