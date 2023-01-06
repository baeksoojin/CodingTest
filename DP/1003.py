# 0을 호출하게 되는 경우(f[0]일때)와 1을 호출하게 되는 경우(f(1)일때)의 개수를 저장할 list를 두개 만든다 
#25분 시작 -> 39분까지 풀기완료.
# 걸린 시간 15분


n = int(input())
result = [(1,0),(0,1)]

for i in range(2,41):
    result.append((result[i-2][0]+result[i-1][0], result[i-2][1] + result[i-1][1]))

for i in range(n):
    a,b = result[int(input())]
    print(a,b)