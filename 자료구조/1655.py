# 첫번째, 두번째 입력에서는 둘다 첫번째로 입렫받은 수를 답으로 설정
# 제한시간은 1초이다. 따라서 정렬은 10^8안에 해결하지 못하기 때문에 우선순위 큐를 활용해야한다.
# heapq 자료구조를 활용해서 mid값을 구해야한다.

# 최소힙중 가장 큰 값과 최대힙중 가장 작은 값을 선택한다.
# 길이가 같을 때 최소힙에 값을 넣음. 길이가 다를 때 최대힙에 값을 넣음 ->(짝수개일때는 중앙에서 작은 값을 선택해야하기때문임)
# 최소힙의 최댓값과 최대힙의 최솟값을 비교하여 최소힙의 최댓값이 더 큰 경우 swap을 진행한다.
# 핵심은 최소힙에서 가장 큰 갑시 mid값이 되는 것으로 알고리즘을 작성해야한다는 것.

import sys
import heapq

input = sys.stdin.readline

n = int(input())
right = []
left =[]

for i in range(n):
    temp = int(input())
    if len(left) == len(right):
        heapq.heappush(left, -temp)
    else:
        heapq.heappush(right, temp)
    if left and right:
        left_max = -left[0]
        right_min =  right[0]
        if left_max > right_min:
           heapq.heappush(left,-heapq.heappop(right))
           heapq.heappush(right,-heapq.heappop(left) )
        
    print(-left[0])

