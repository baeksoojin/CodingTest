# 떡볶이 떡을 자르고 남은 떡의 길이가 m이 만들어질 수 있는 절단기 높이의 최대값

# 절단기 높이를 바꿔가며 떡의 합의 길이를 체크하고 같아질 때 해당 절단기의 높이를 출력[ 특정 조건을 만족하는 절단기의 높이 *"탐색"* 문제 ] -> 절단기의 높이를 크게 잡고 줄여나가게하며 체크

n,m=map(int, input().split())
n_list = list(map(int, input().split()))

def bs(start, end, mid):

    for i in range(n):
        if n_list[i]//mid>=1:
            sum += n_list[i]%mid   

    #떡이 더 필요한 경우 -> 절단기 크기를 줄여야함
    if sum < m:
        bs(start,mid, (start+mid)//2 )
    elif sum>m: #절단기 크기를 늘려야하는 경우
        bs(mid, end, (mid+end)//2)
    else: #현재 절단기 크기로 떡을 만들 수 있을 때
        print(mid)
        return mid


bs(0,max(n_list), max(n_list)//2) # 절단기 크기를 mid로 넘김

## input
# 4 6
# 19 15 10 17

##output
# 15
