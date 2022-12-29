n = int(input())

count = [9999]*5001

count[3] = 1
count[5] = 1

for i in range(3,n+1):
    for j in range(3, (i+1)//2+1):
        count[i] = min(count[i], count[j] + count[i-j])

if count[n]==9999:
    print("-1")
else:
    print(count[n])

# 5키로를 먼저 선택하는 그리디로도 풀 수 있는 문제
# 그리디 풀이 : 5키로의 몫의 수까지 0부터 무게에서 빼고 나머지를 3키로짜리로 만들 수 있는지 체크 -> 만약에 없다면 -1.
# 만약에 3,5키로가 아니라 3,4,5키로로 3가지 경우가 주어진다면 DP를 적극 활용. 다만 여기서는 그리디로 풀어야 시간을 확 줄일 수있음.