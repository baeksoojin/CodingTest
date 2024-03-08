'''
회의실 배정

회의실의 시작시간과 끝 시간이 있을 때, 회의가 겹치지 않으면서 회의실을 사용할 수 있는 최대개수
-> 끝나는 시간이 빠르도록 정렬. -> 우선순위를 부여 (그리디, 정렬)
-> 그 다음 것중에서 시작시간이 끝나는 시간 이후이거나 같은 경우에 배정한다. 
'''

import sys

input = sys.stdin.readline

n = int(input())

times = []

for i in range(n):
    a,b = map(int, input().split())
    times.append((a,b))

#times = sorted(times,key = lambda x: (x[1], x[0])) #끝시간에 맞춰서 정렬하기
times.sort(key = lambda x: (x[1], x[0]))

count = 0
before_end_time =0

for case in times:
    if case[0] >= before_end_time:
        count +=1
        before_end_time = case[1]

print(count)


# 틀린 이유 : 시작시간이 동일한 경우, 끝나는시간이 빠른것을 선택해야함. -> 끝나는 시간 정렬 후 , 그 상태에서 시작시간을 재정렬해야함