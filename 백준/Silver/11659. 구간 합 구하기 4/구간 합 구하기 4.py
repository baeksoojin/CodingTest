
import sys
input = sys.stdin.readline

n,m=map(int, input().split())

n_list = [0]+list(map(int, input().split()))
sum = [0]*100001
sum[1] = n_list[1]

for i in range(2,n+1):
    sum[i] = n_list[i]+sum[i-1]

for i in range(m):
    a,b = map(int, input().split())
    print(sum[b]-sum[a-1])