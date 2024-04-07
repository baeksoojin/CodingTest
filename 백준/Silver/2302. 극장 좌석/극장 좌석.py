
n = int(input())
m = int(input())

vip = set() # 고정되어얗니, 앞앞의 경우는 더하지 않음. ( 이전 경우의 수와 동일) / vip 다음위치도 앞자리와 못 바꾸니까 (이전 경우와 동일)
for i in range(m):
    number = int(input())
    vip.add(number)
    vip.add(number+1)

count = [0]*(n+1)

count[0] = 1 # 2번째를 계산하기 위해
count[1] = 1

for i in range(2,n+1):
    if i in vip:
        count[i] = count[i-1]
    else:
        count[i] = count[i-1] + count[i-2]

print(count[n])
