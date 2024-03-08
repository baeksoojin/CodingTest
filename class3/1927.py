'''
배열에 자연수를 넣고 배열에서 가장 작은 값을 출력하고 배열에서 값을 제거

0 -> 가장 작은 값을 출력하고 제거
heappop -> 가장 작은 원소를 차례대로 제거한다.
참고 ) 이때, 최대힙을 구하려면 heappop(heap, (-item , item)) -> -item이기에 큰 값이 가장 작아서 우선순위가 큰 값으로 부여되고 값은 index 1을 통해서 접근

'''

import heapq
import sys
input = sys.stdin.readline

heap = []

n = int(input())

for i in range(n):
    num = int(input())
    
    if num == 0: # pop
        if len(heap) == 0: #없는데 heappop을 진행
            print("0")
        else:
            value = heapq.heappop(heap) # 있다면 최소값을 꺼내고 print
            print(value)

    else: # push
        
        heapq.heappush(heap, num)





