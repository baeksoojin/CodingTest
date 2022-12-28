# 수 찾기 -> 탐색문제 -> 주어지는 수의 개수가 100000이고 찾아야하는 수는 100000. -> 시간복잡도 n**2에서 nlogn으로 이진탐색 적용

n = int(input())
n_list = sorted(list(map(int,input().split())),reverse=False)
m = int(input())
m_list = list(map(int,input().split()))



def bs(start, end, mid, target):

    if start > end:
        print("0")
        return

    if n_list[mid] == target:
        print("1")
        return
    elif n_list[mid] < target:
        bs(mid+1,end,(mid+1+end)//2, target)
    else:
        bs(start,mid-1,(start+mid-1)//2, target)


for value in m_list:
    bs(0,n-1,(n-1)//2,value)
