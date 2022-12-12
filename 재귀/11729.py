#하노이탑

n = int(input())
def hanoi(n,start, end):
    if n==1:
        print(start, end)
        return
    hanoi(n-1, start, 6-start-end) # 가장 큰 원판을 제외한 나머지를 2번째 자리로 옮기기
    print(start, end) # 가장 큰 원판을 옮기기
    hanoi(n-1, 6-start-end, end) # 옮겨놓은 원판들을 end로 해당 위치에서 다 옮겨야함

print(2**n-1)
hanoi(n, 1,3)