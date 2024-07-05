'''
공유기 설치

차이가 적도록 해야하니까 정렬하고 s- > 0 / e -> n-1
s와 e사이의 거리가 가장 적도록하기! (s<=e)까지 가능.
두점사이의 거리가 최소가 되도록하는 것 
이때, 두점상의 거리를 start + end 를 2로 나눈 Mid로 지정 
그것보다 거리가 큰 공유기의 개수가 c개 이상이 가능하다? 거리가 늘어도 되는지 체크.
c개보다 작다 ? 거리가 줄어들어야함.
가능한 거리 중에서 가장 최댓값 -> mid로 갱신

거리 -> 이분탐색의 대상으로 설정

'''

import sys

input = sys.stdin.readline

n, c = map(int, input().split())

n_list = []
for _ in range(n):
    n_list.append(int(input()))

n_list.sort()

start, end = 1, n_list[-1] - n_list[0]

while start<=end:

    mid = (start + end )//2
    current = n_list[0] # 첫 집부터 탐색
    
    cnt = 1
    for value in n_list:
        if value >= current + mid:
            cnt+=1
            current = value #  mid보다 크거나 같으면서 mid+첫번째 current가 만드는 값이 가장 작은 값이여야하기에

    if cnt >= c:
        start = mid+1
        result = mid
    else:
        end = mid -1
print(result)









