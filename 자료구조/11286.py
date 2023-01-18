'''
절댓값 힙

기본이 최소힙이니까 양수를 넣어서 꺼내야함
절댓값이 가장 작은 값을 출력 -> 힙을 두개 만들기
첫번째 힙 -> 음수인 숫자들만 넣을 힙으로 양수로 변환해서 넣어놓고 들어간 값으로 값이 최소인지 두번째 힙과 비교
두번쩨 힙 -> 양수를 넣고 그대로 값을 넣고 꺼내서 첫번째 힙이랑 비교.
첫번째와 두번째 힙의 최소값이 같을 경우, 둘다 제거 하나가 더 작을 때 그 값이 모든 힙에서 다 없어질 때까지 제거한다.

'''

import sys
import heapq
input = sys.stdin.readline

n = int(input())

heap1 = []
heap2 = []

for i in range(n):
    num = int(input())

    if num==0:#가장 작은 값을 제거
        if len(heap1)==0 and len(heap2)==0:
            print("0")
        elif len(heap1)==0:
            print(heapq.heappop(heap2))
        elif len(heap2)==0:
            print(-heapq.heappop(heap1))
        else: #두개의 힙 모두 값이 존재할 때
            if heap1[0] > heap2[0]:
                print(heapq.heappop(heap2))
            elif heap1[0] < heap2[0]:
                print(-heapq.heappop(heap1))
            else:
                print(-heapq.heappop(heap1)) #절댓값이 똑같을 경우 원래 숫자가 -였던 값을 저장한 heap1에서 뺀다
    else:
        if num<0:
            heapq.heappush(heap1, -num)
        else:
            heapq.heappush(heap2, num)
        


        