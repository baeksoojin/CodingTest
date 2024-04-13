'''
배열돌리기
'''

from collections import deque
n,m,r = map(int, input().split())
arr = []
new_arr = [[0]*m for _ in range(n)]
q = deque()

for i in range(n):
    arr.append(list(input().split()))

loops = min(n,m)//2
for i in range(loops):
    q.clear()
    q.extend(arr[i][i:m-i])
    # print(arr[i][i:m-i])
    q.extend([row[m-i-1] for row in arr[i+1:n-i-1]])
    # print([row[m-i-1] for row in arr[i+1:n-i-1]])
    q.extend(arr[n - i - 1][i:m - i][::-1])
    # print(arr[n - i - 1][i:m - i][::-1])
    q.extend([row[i] for row in arr[i + 1:n - i - 1]][::-1])
    # print([row[i] for row in arr[i + 1:n - i - 1]][::-1])
    # print(q)

    q.rotate(-1*r)

    for j in range(i, m - i):  # 상
        new_arr[i][j] = q.popleft()
    for j in range(i + 1, n - i - 1):  # 우
        new_arr[j][m - i - 1] = q.popleft()
    for j in range(m - i - 1, i - 1, -1):  # 하
        new_arr[n - i - 1][j] = q.popleft()
    for j in range(n - i - 2, i, -1):  # 좌
        new_arr[j][i] = q.popleft()

for i in range(n):
    for j in range(m):
        print(new_arr[i][j], end=" ")
    print()
