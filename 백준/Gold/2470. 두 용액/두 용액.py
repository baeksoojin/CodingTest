'''
용액 두개를 혼합해 나온 합이 0에 가장 가까운 용액
그 때의 두 용액을 찾기. 오름차순으로 출력

합이 min보다 크다면? start+1
합이 min보다 작거나 같다? end+1

start와 end가 동일하면 안 됨. -> end+1

이건 사실 둘다 0으로 세팅하면 복잡해지는 문제 왜냐면, start와 end가 같아지면 추가코드를작성해야함

'''

import sys

input = sys.stdin.readline
answer1 = answer2 = 0 # 2개 저장
n = int(input())

nums = list(map(int, input().split()))
min_temp = 10e9
start =0
end = n-1
value = 0

nums.sort()

while start<end:

    value = abs(nums[start] + nums[end])

    if value < min_temp:
        min_temp = value
        answer1 = nums[start]
        answer2 = nums[end]
        if value ==0:
            break
    # 절댓값이 큰 수를 버리기
    if abs(nums[start]) < abs(nums[end]):
        end-=1
    else:
        start+=1
if answer1 == answer2 and answer1 ==0:
    print(nums[start], nums[end])

if answer1 > answer2:
    answer1 , answer2 = answer2, answer1

print(answer1, answer2)