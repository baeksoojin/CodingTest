
n,m = map(int, input().split())

n_list = list(map(int, input().split()))

start, end = 1, max(n_list)
last = 0

def get_total_tree_by_mid(mid):

    total = 0
    for i in range(n):
        total += (n_list[i] - mid if n_list[i] >mid else 0)

    return total


while start<= end:

    mid = (start + end)//2

    total_tree_by_mid = get_total_tree_by_mid(mid)

    if total_tree_by_mid >= m: # 구한 총 나무가 가지고가고싶은 나무보다 클 때 -> 
        start = mid+1
        last = mid
    else: # 구한 나무가 가지고 가고 싶은 값보다 작다면 더 키워야하기에 h를 낮워야함
        end = mid-1


    
print(last)


    


