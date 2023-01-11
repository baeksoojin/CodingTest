'''

2시 30분 시작 

최대힙을 이용해서 연산을 지원.

1. 0 일때는 가장 큰 값을 출력하고 배열에서 제거 (비어있다면 0을 출력) -> heappop을 사용하라는 것
2. 0이 아닌 수일때는 값을 넣으면 됨.

'''
import sys
import heapq

input = sys.stdin.readline
n = int(input())

result =[]

for _ in range(n):
    num = int(input())
    if num==0:
        if len(result) ==0:
            print("0")
        else:
            print(-heapq.heappop(result))
         
    else:
        heapq.heappush(result, -num)
