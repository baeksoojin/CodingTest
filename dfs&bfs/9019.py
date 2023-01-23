'''
결국에는 최솟값을 찾는 문제인데 DSLR을 적절하게 조합하여 명령어 개수에 따라 될 수 있는 경우를 모두 체크해나가면 되는 것

DSLR
D -  다음 명령어는 DSLR중 하나 ...
S -  다음 명령어는 DSLR중 하나 ...
L -  다음 명령어는 DSLR중 하나 ...
R -  다음 명령어는 DSLR중 하나 ...
위와 같이 되기 때문에 bfs를 사용해서 체크하도록 한다.

'''

import sys
from collections import deque
input = sys.stdin.readline


t = int(input())


def bfs(queue, visited, opers, after):

    while(queue):
        num = queue.popleft()
        oper = opers.popleft()

        # DSLR을 탐색
        num_dic = {}
        num_dic["D"] = num*2
        num_dic["S"] = num-1
        num_dic["L"] = (num%1000)*10 + num//1000
        num_dic["R"] = (num//10) + (num%10)*1000

        if num_dic["D"]>9999:
            num_dic["D"] = num_dic["D"]%10000
        if num_dic["S"] == -1:
            num_dic["S"] = 9999
        
        # check
        for key, value in num_dic.items():
            if value==after:
                print( (oper + key)[1:])
                return (oper + key)[1:]
            else: # DSLR 너비우선탐색
                if visited[value]==False: 
                    queue.append(value)
                    opers.append(oper + key)
                    visited[value]=True
            
        

for i in range(t):
    before, after = map(int, input().split())

    queue = deque()
    opers = deque()
    visited = [False]*(10001)
    
    queue.append(before)
    opers.append(" ")
    visited[before] = True
    bfs(queue, visited, opers,after)

# python3로 풀었는데 시간초과 -> pypy는 맞았습니다!
# 스터디때 함께 풀 문제로 공유해서 시간초과 해결해보기!
