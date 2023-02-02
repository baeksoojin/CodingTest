'''
1이나 0이 특정 범위에서 나온 개수를 count변수에 저장하고 둘중 하나만 0일때는 분할정복을 멈추고
둘다 count값이 0이 아닌 정수일때 분할정복을 다시시도한다.
'''


import sys
input = sys.stdin.readline

n = int(input())

graph = []*n

for i in range(n):
    graph.append(list(map(int, input().split())))

c_blue = 0
c_white = 0

def counting(x,y,z):
    global c_white
    global c_blue

    white=0
    blue=0
    for i in range(z):
        white += graph[x+i][y:y+z].count(0)
        blue += graph[x+i][y:y+z].count(1)
    #print(white, blue)
    if white==0 or blue==0:
        if white==0:
            c_blue+=1
        else:
            c_white+=1
        return
    else:
        counting(x,y,z//2)
        counting(x,y+z//2,z//2)
        counting(x+z//2,y,z//2)
        counting(x+z//2, y+z//2, z//2)

counting(0,0,n) 
print(c_white)
print(c_blue)