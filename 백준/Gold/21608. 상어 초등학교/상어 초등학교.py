n = int(input()) # n*n이 테이블

# 초기화 : 학생번호랑 학생이 좋아하는 4명 -> 순서가 중요하지 않으니 set으로 설정
student_numbers = []
student_like_numbers = [] # 4명을 student_number의 index와 동일한 Index에 집합으로 저장
for i in range(n**2):
    line = list(map(int, input().split()))
    student_numbers.append(line[0])
    student_like_numbers.append(set(line[1:]))

# 초기화 : 학생을 저장할 배열 student를 초기화
student = [[0] * n for _ in range(n)]

direct = [(0,1), (0,-1), (1,0), (-1,0)]

# 1. 학생을 한명씩 돌면서 체크
for s in range(n**2):
    current_student = student_numbers[s]
    current_like_numbers = student_like_numbers[s]
    s_temp = [] # like수와 empty 수, i, j를 저장할 튜플을 담을 공간

    # 1-1 자리 하나씩 탐색해서 s_temp를 update
    for i in range(n):
        for j in range(n):
            like = 0
            empty = 0
            if student[i][j] == 0: # student가 앉지 않은 자리만 가능
                # 인접한 4곳을 탐색하고 like,empty를 초기화
                for dir in direct:
                    next_i = i + dir[0]
                    next_j = j + dir[1]
                    if 0<=next_i<=n-1 and 0<=next_j<=n-1:
                        # 좋아하는 사람이 있는지 체크
                        if student[next_i][next_j] in current_like_numbers:
                            like+=1
                        # 비어있는 자리인지 체크
                        if student[next_i][next_j] == 0:
                            empty+=1
                s_temp.append((like, empty, i, j))

    # 1-2. 2중 for문을 돌면서 만족하는 좌석을 찾음
    s_temp.sort(key = lambda x:(-x[0],-x[1],x[2],x[3]))
    # print(s_temp)
    s_i = s_temp[0][2]
    s_j = s_temp[0][3]
    # print(current_student , "의 좌석 -> " , s_i, s_j)
    student[s_i][s_j] = current_student


# 2. 세팅된 좌석에서 만족도를 구하기

satisfied = 0
for i in range(n):
    for j in range(n):
        current_student = student[i][j]
        student_index = student_numbers.index(current_student)
        current_like_numbers = student_like_numbers[student_index]
        like = 0
        for dir in direct:
            next_i = i + dir[0]
            next_j = j + dir[1]
            if 0 <= next_i <= n - 1 and 0 <= next_j <= n - 1:
                # 좋아하는 사람이 있는지 체크
                if student[next_i][next_j] in current_like_numbers:
                    like += 1
        if like == 1:
            satisfied +=1
        elif like ==2:
            satisfied += 10
        elif like ==3:
            satisfied += 100
        elif like ==4:
            satisfied += 1000

print(satisfied)