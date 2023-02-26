'''
n개의 정수를 줬을 때 합이 s가 되도록 하는 부분수열의 개수를 구해야함
부분수열의 합. 부분 수열을 비트마스킹
따라서 O(N^N)의 시간복잡도를 가지는 백트래킹보다는 부분 집합 처리로 비트마스킹을 활용하는 연습을 해야함

'''

n, s = map(int, input().split())

n_list = list(map(int, input().split()))
count=0

# 부분집합으로 만들 수 있는 가잗 큰 경우(11111)모두를 선택한 경우 -> 모두 선택되는 경우로 (1<<5)-1

for i in range(1,1<<n):
    sum=0
    for j in range(n):
        if i&(1<<j):
            sum+=n_list[j]
    if sum==s: count+=1

print(count)




