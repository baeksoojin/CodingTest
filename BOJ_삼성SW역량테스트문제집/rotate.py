# 회전 1) *을 사용해서 unpacking을 진행. -> 직사각형, 정사각형 모두 적용 가능.
arr  = [[1,2],[3,4]]

# for j in zip(*arr[::-1]):
#     print(j)

'''
1. 90도 시계방향 회전

[3,4] [1,2]를 zip -> [3,1],[4,1]로 90도 오른쪽으로 회전하게됨
'''
print(list(map(list,zip(*arr[::-1]))))
rotate_90 = list(map(list,zip(*arr[::-1])))

'''
2. 180도 시계방향 회전
90도씩 두번 회전?
'''

rotate_180 = list(map(list,zip(*rotate_90[::-1])))
print(rotate_180)

'''
3. 270도 회전은? 90도 회전을 3번 하면 됨
'''

rotate_270 = list(map(list, zip(*rotate_180[::-1])))
print(rotate_270)

# 회전 2) for문을 돌며 i,j를 가지고 놀기
'''
90도 회전) (0,0)이 (0,1)으로 가는 점 -> 새로운 배열(j, n-i-1)위치는 기존 위치(i,j)의 값을 가짐 
직사각형일땐, 가로 세로가 변경되어서, -> n,m을 변경해줘야함. (j, m-i-1)로 기존 (i,j)값을 저장한다.
'''
n=2
# 시계 방향 90 (= 반시계 방향 270)
new_90 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_90[j][n - i - 1] = arr[i][j]
print(new_90)

