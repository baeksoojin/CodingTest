#최소한 index가 하나이상 떨어진 곳을 선택이 가능함 & 최대한 많은 식량을 얻어야함. 식량창고에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값 구하기

# 5시 12분 시작 -> 목표 시간 :42분까지 풀기 -> 결과 : 5시28분 완료.

# 풀이방법
# index 0부터 시작 혹은 1부터 시작하기. => for문을 2부터 체크하고/ index-2로 0또는 1을 불러오며 sum.
# 현재 index의 방을 털고 -2 index방을 터는 경우 / 혹은 현재 방을 털지 않고 그 이전 방을 터는 경우. => 더 큰것을 선택
n = int(input())
n_list = list(map(int, input().split()))

food = [0]*100 #식량창고는 최대 100개

food[0] = n_list[0]
food[1] = max(n_list[1], n_list[0])

for i in range(2, n):
    food[i] = max(food[i-2]+ n_list[i] , food[i-1])

print(max(food))