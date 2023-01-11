'''

2시 53분 시작 -> 59분 풀이 완료.

줄을 서는 사람들이 기다리는 시간을 가장 적게 가져가려면 앞의 사람을 적게 기다리는 것이다. 
앞의 사람 순서대로 가장 빠르게 일을 처리하는 사람을 두고 줄을 서면 각 사랍이 돈을 인출하는데 필요한 최솟값을 구할 수 있다.

다음 사람은 남은 것중에 "가장 작은 것을 선택한다"는 것을 보아 그리디이다.

'''

import sys
input = sys.stdin.readline

n = int(input())
n_list = sorted(list(map(int, input().split())))
# print(n_list)

sum_list = [0]*n
sum_list[0] = n_list[0]
for i in range(1,n):
    sum_list[i] = sum_list[i-1]+n_list[i]

print(sum(sum_list))