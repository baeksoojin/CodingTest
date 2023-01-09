# 0이라면 가장 작은 값을 출력하고 빼는 연산을 수행
# 0이 아닌 정수라면 해당 값을 넣는 연산을 수행
# heapq는 최소heap tree 자료구조로 가장 작은 값을 가장 root node(intex 0)에 보관한다.

import sys, heapq
input = sys.stdin.readline

n = int(input().strip())
n_list=[]


for _ in range(n):
    x = int(input().strip())

    if x ==0:
        if len(n_list)==0:
            print("0")
        else:
            print(heapq.heappop(n_list))
    else:
        heapq.heappush(n_list, x)
