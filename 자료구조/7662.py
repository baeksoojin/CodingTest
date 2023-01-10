'''
2시 44분 시작

데이터를 삭제할 때 연산의 명령에 따라서 우선순위가 가장 높은 데이터 또는 가장 낮은 데이터 중 하나를 삭제한다.

우선순위 큐

데이터를 삽입
데이터를 삭제 -> 1. 우선순위가 가장 높은 것을 삭제, 2. 우선순위가 가장 낮은 것을 삭제

heapq를 두개사용해서 하나는 최솟값을 뽑을 용도, 하나는 최댓값을 뽑을 용도로 사용하면 될 것 같음.
1.번의 연산이든 2.번의 연산이든 연산 후에는 두개의 heapq에서 삭제한 데이터를 모두 지워줘야하는 과정이 필요해보임.

'''

import sys
import heapq
input = sys.stdin.readline

n = int(input())

for _ in range(n):

    minh = []
    maxh =[]
    
    count = int(input())
    for _ in range(count):
        o, num = map(str,input().split())
        if o=="I":
            heapq.heappush(minh, int(num))
            heapq.heappush(maxh, -int(num))
        else:
            if len(minh)==0:
                continue
            if num == "-1": #최솟값을 삭제
                del_num = heapq.heappop(minh)
                maxh.remove(-del_num)
            else:#최댓값을 삭제
                del_num = -heapq.heappop(maxh)
                minh.remove(del_num)
    
    if not minh:
        print("EMPTY")
    else:
        max = -heapq.heappop(maxh)
        min = heapq.heappop(minh)
        print(max, min)