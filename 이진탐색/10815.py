'''
상근이가 가지고 있는 카드가 주어진 수중에서 존재하는지 판단.

수를 탐색하는 것으로 이진탐색을 진행해야하는데, 이중루프를 사용하면 500000*500000이 될 수 있기에 시간초과 -> 이진탐색을 진행한다.

'''

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

def find_target(start,end,target):
    
    if start>end:
        print("0", end=" ")
        return

    mid=(start+end)//2

    if n_list[mid] > target:
        find_target(start,mid-1, target)
    elif n_list[mid] < target:
        find_target(mid+1, end, target)
    else:
        print("1", end=" ")
        return

for target in m_list:
    find_target(0,n-1, target)