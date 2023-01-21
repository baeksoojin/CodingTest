'''
3시 15분 시작

주어진 배열의 수를 모두 똑같은 수(k)로 "최소시간에" 걸쳐서 만드는 과정에서 나올 수 있는 최대 k의 값을 구하기


특정위치에서 -1을 할경우 time을 2증가 
특정위치에서 +1을 할 경우 time을 1증가

이때 값이 256을 초과할 수 없고 -1이 가능한 블럭은 b개부터 시작.
만약 2개의 과정을 했을 때 같은 최소시간이 걸릴 경우, +1을하는 것으로 하기
--
최소시간을 만들기 위해서 우선 같은 size로 된 애들끼리 묶어서 생각해야함.
만약에 그룹끼리 최대 차이가 3이라면 가장 작은 그룹의 수로 만드는 것부터 시작해서 가장 큰 그룹의 수로 만드는 것의 경우의 수를 돌면서 최소 시간을 찾아야함.
----
기존코드에서 시간초과가 나서 계산을 for문을 돌면서 하는게 아니라 -1을 할경우의 count값과 +1을 할경우의 count값을 다 구하고 이후에 한번에 체크하는 방식으로 변경

'''

'''
import sys
input = sys.stdin.readline

n,m,b = map(int, input().split())

blocks = []
temp_list = []
for i in range(n):
    blocks.append(list(map(int, input().split())))
    temp_list += blocks[i]

level_list = list(set(temp_list))
min_level, max_level = min(level_list), max(level_list)
max_level = max(max_level,256)

time = 1e9
h = 0
for level in range(min_level, max_level+1): #가능한 블럭의 level을 설정

    b_temp = b
    flag = True
    temp_time=0
    for i in range(n):
        for j in range(m):
            #만약 현재 위치에 5(6)개 만들려는 level이 6(5)개라면 하나를 가져와야하기에 b_temp가 1개보다 많아야함.(하나를 b_temp로 빼야함)
            if level > blocks[i][j]: # b_temp에서 하나 가져옴.
                b_temp = b_temp - (level-blocks[i][j])
                temp_time += (level-blocks[i][j])*1
            elif blocks[i][j]!=level and level<blocks[i][j]:
                b_temp = b_temp + (blocks[i][j]-level)
                temp_time += (blocks[i][j]-level)*2
            else:
                continue
    if b_temp<0:
        continue
    else:
        if time >= temp_time:
            time = temp_time
            h = level
print(time,h)
=>시간초과
'''

import sys
input = sys.stdin.readline

n,m,b = map(int, input().split())

blocks = []
temp_list = []
for i in range(n):
    blocks.append(list(map(int, input().split())))
    temp_list += blocks[i]

level_list = list(set(temp_list))
min_level, max_level = min(level_list), max(level_list)
max_level = max(max_level,256)

time = 1e9
h = 0
for level in range(min_level, max_level+1): #가능한 블럭의 level을 설정

    b_temp = b
    flag = True
    m_count,p_count=0,0
    for i in range(n):
        for j in range(m):
            #만약 현재 위치에 5(6)개 만들려는 level이 6(5)개라면 하나를 가져와야하기에 b_temp가 1개보다 많아야함.(하나를 b_temp로 빼야함)
            if level > blocks[i][j]: # b_temp에서 하나 가져옴.
                m_count += (level-blocks[i][j])
            else:
                p_count += (blocks[i][j]-level)
    if b+p_count>=m_count:
        if p_count*2+m_count<=time:
            time = p_count*2+m_count
            h = level
print(time,h)

# 다만 pypy만 합격함