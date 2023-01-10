'''
 특정 영역안의 0의 개수를 카운트해서 해당 영역의 개수와 같은지 체크한다(모두 같은색인지 체크)
 존재한다면 -> 다시 위의 과정을 반복하는데 이때 영역을 또 4등분해서 같은 함수를 4번 돌게한다.
 존자해지 않는다면 -> 파란색 종이의 개수를 하나 증가시키고 return한다.
'''

import sys
input = sys.stdin.readline

n = int(input())

graph = []*n

for i in range(n):
    graph.append(list(map(int, input().split())))

counting_blue = 0
counting_white = 0

def counting(x,y,z):
    global counting_white
    global counting_blue
    # 특정영역에 0이 포함되어 범위를 좁혀 탐색해야하는 경우
    white=0
    blue=0
    for i in range(z):
        white += graph[x+i][y:y+z].count(0)
        blue += graph[x+i][y:y+z].count(1)
    #print(white, blue)
    if white==0 or blue==0:
        if white==0:
            counting_blue+=1
            #print("counting_blue",counting_blue)
        else:
            counting_white+=1
            #print("counting_white",counting_white)
        return
    else:
        counting(x,y,z//2)
        counting(x,y+z//2,z//2)
        counting(x+z//2,y,z//2)
        counting(x+z//2, y+z//2, z//2)

counting(0,0,n) 
print(counting_white, counting_blue)

'''
처음에 counting(0,0,8)로 n을 8로 고정하고 제출하고 계속 뭐가 틀렸는지 찾다가 10분정도 더 썼다....^^
그리고 print값을 주석처리를 안 하고 로그도 출력하게 해놔서 출력초과가 떴고
위의 실수 두개를 제거하니 맞았습니다가 나왔다!
위의 풀이는 자료구조로 분리해놓은 1074번을 풀어봤기에 그래도 빠르게 풀 수 있었다.
'''