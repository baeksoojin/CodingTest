
'''
삼각형 아래로 내려오면서 최댓값을 선택해야함.

현재위치에서 왼쪽위에 있는 수와 오른쪽 위에 있는 수중 큰 값을 선택
'''
import sys
input = sys.stdin.readline

n = int(input())

tri = []

for i in range(n):
    tri.append(list(map(int, input().split())))

for i in range(1,n):
    for j in range(0,i+1):
        if j==0:
            tri[i][j] = tri[i-1][0] + tri[i][j]
        elif j==i:
            tri[i][j] = tri[i-1][j-1] + tri[i][j]
        else:
            tri[i][j] = max(tri[i-1][j-1], tri[i-1][j])  + tri[i][j]
        
# print(tri)
print(max(tri[n-1]))

