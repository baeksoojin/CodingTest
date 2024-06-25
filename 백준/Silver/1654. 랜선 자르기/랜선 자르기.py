import sys

n, m= map(int,input().split())

n_list = []

max_num = -1
for i in range(n):
    num = int(sys.stdin.readline())
    n_list.append(num)
    if num > max_num:
        max_num = num

start,end = 1, max_num
last = -1

def total_lan_count(cable):
    count = 0
    for i in range(n):
        count+= n_list[i] // cable

    return count

while start<=end:

    mid = (start+end)//2        

    total_lan_by_mid = total_lan_count(mid)

    if total_lan_by_mid >= m:
        last = mid
        start = mid+1
    elif total_lan_by_mid < m: # 케이블 개수가 더 많아야함 -> 쪼개는 단위를 줄여야함
        end = mid - 1


print(last)
