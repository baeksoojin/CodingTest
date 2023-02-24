'''
5시 38분 시작

2007년 x월 Y일은 무슨 요일일까?

'''

# 우선 해당 날짜까지 며칠 지났는지 계산

m, d = map(int, input().split())

month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
month_sum = [0]*(13)
results = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

for i in range(1,13):
    month_sum[i] = month_days[i] + month_sum[i-1]

total_days = month_sum[m-1]+d

print(results[total_days%7])
