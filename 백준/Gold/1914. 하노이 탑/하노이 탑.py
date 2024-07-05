
def move(start, end):
    print("{0} {1}".format(start, end))


def hanoi(n, start, end, mid): # n개의 묶음을 start -> end

    if n==1:
        move(start, end)
        return

    # 가장 밑에 있는 것을 제외한 모든 것을 mid로 옮기기
    hanoi(n-1, start, mid, end)

    # 가장 밑에 있는 것을 end지점으로 옮기기
    move(start, end)

    # mid에 있던 모든 것을 end로 옮기기
    hanoi(n-1, mid, end, start)

n = int(input())
# 1번당 재귀를 2번 호출 -> 재귀의 경우 2의 시행횟수(5개를 옮겨야하면 5번 시행) -> 2**5

print(2**n - 1)

if n<=20:
    hanoi(n,1,3,2)