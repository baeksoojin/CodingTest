# # 3시 15분 시작 -> 4시10분에 제출 (testcase 정답확인) -> 메모리초과

# # 다이나믹 프로그래밍으로 우선 입력받은 값을 디폴트로 저장했다가 이후에 더 많은 시간을 가지고 있는 것에대한 회
# # 문제에 대한 아이디어를 생각하는데만 30분을 사용했는데 dp문제에 빨리 익숙해져서 빠르게 생각해낼 필요가 있어보임

# # 2차원 리스트를 구현해야함.

# import sys
# input = sys.stdin.readline

# n = int(input())

# n_list = []
# max_num =0
# min_num = 0
# for i in range(n):
#     a,b = map(int, input().split())
#     n_list.append((a,b))
#     min_num = min(min_num, a)
#     max_num = max(max_num, b)

# # 2차원 리스트를 만들때 n+1행 max_num - min_num +1 개의 열을 만들어서 사용한다.

# max_result = [[0]*(max_num+1) for _ in range(n+1)]

# for i in range(1,n+1):
#     a,b = n_list[i-1]
#     for j in range(0,b):
#         max_result[i][j]= max_result[i-1][j]
#     for j in range(b,max_num+1):
#         max_temp =0
#         if a==0:
#             max_temp = max_result[i-1][b]
#         else:
#             max_temp = max(max(max_result[i][:a])+1, max_result[i-1][b])
#         max_result[i][j] = max_temp

# # print(max_result)
# print(max(max_result[n]))

# # 시간초과와 메모리초과가 나올 것 같음 -> 2^31승일때... 

# n = int(input())
# cases =[]

# for _ in range(n):
#     a,b=map(int, input().split())
#     cases.append((a,b))

# cases = sorted(cases, key = lambda x : cases[1])

# count = 0
# before_end_time =0

# for case in cases:
#     if case[0] >= before_end_time:
#         count +=1
#         before_end_time = case[1]
#     else:
#         continue

# print(count)

# 틀림 
# 끝나는 시간과 시작 시간이 같을 경우에 반례가 됨
# ex)
# 2
# 2 2
# 1 2


n = int(input())
cases =[]

for _ in range(n):
    a,b= map(int, input().split())
    cases.append((a,b))

cases = sorted(cases, key = lambda case : (case[1], case[0]))

# 끝나는 시간이 같을 경우, 다음 우선순위로 시작시간을 두어 재정렬하여 끝나는 시간이 같을 경우에 시작시간이 빠른것을 선택하고 이후에 끝나는 시간이 같았던 다른 경우를 선택하여 다시 counting을 하게 해준다.
 

count = 0
before_end_time =0

for case in cases:
    if case[0] >= before_end_time:
        count +=1
        before_end_time = case[1]

print(count)
