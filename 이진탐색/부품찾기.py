# 10시2분 시작[제한시간 30분] -> ~ 10시 17분
# 탐색 문제. n이 1,000,000으로 그냥 for문은 낭비. 

import sys

n = int(input())
n_list = list(map(int,sys.stdin.readline().strip().split()))
n_list.sort(reverse=False)

m = int(input())
m_list = list(map(int,sys.stdin.readline().strip().split()))

def bst(array, target, start, end):
    while(start<=end):
        mid = start+ end
        #같을 때
        if target==array[mid]:
            return "yes"
        elif target < array[mid]:
            end = mid-1
        else:
            start = mid+1
    return "no"

for target in m_list:
    print(bst(n_list, target, 0, n-1), end=" ")

# 시간복잡도는 n개를 정렬하기 위해서 nlogn이 요구됨. m개를 logn 해서 mlogn이 요구됨 ->O( (n+m)logn )
# 정렬을 사용할 수도 있음