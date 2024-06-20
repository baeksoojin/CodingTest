n = int(input())

s_diff = [0]*(n)

for i in range(n):
    s_diff[i] = int(input())
    
total = sum(s_diff) 

start = end = 0
result = 0

min_now = 0
        
while start <= end and end < n:
    
    min_dist = min(min_now, total - min_now) # 둘 중 작은게 두 점사이의 길이
    result = max(min_dist, result)

    if min_now == min_dist: # 현재가 가장 작은 값이였다면
        min_now += s_diff[end]
        end+=1
    else:
        min_now -= s_diff[start]
        start +=1
print(result)

