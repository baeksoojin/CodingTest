# for문으로 모두 탐색해버리기엔 시간초과
# 정렬 후 이진탐색

import sys
imput = sys.stdin.readline

n = int(input())
n_list = sorted(list(map(int, input().split())), reverse=False)
m = int(input())
m_list = list(map(int, input().split()))

def binary_search(start, end, mid, m):

    if start>end:
        print("0")
        return
    
    if m>n_list[mid]:
        binary_search(mid+1, end, (mid+end+1)//2, m)
    elif m< n_list[mid]:
        binary_search(start, mid-1, (start+mid-1)//2, m)
    else:
        print("1")
        return

for m in m_list:
    binary_search(0,n-1, (n-1)//2, m)