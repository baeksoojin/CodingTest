'''

0을 기준으로 왼쪽을 마이너스(알칼리) 그리고 오른쪽을 양수로 설정하고 정렬한다.

-99 -2 -1 4 98
두 용액의 차이가 가장 적은 것을 선택해야함.


-95
-1
2
96
3 
97 등등


------

두개의 합의 절댓값을 이전값과 비교해서 start, end를 바꿔주는건데 
중간에 이전값과의 비교만생각해서 두개의 합인 total에 절댓값을 적용했음...
그러면 당연히 

if total < 0:
    start += 1

이게 실행이 안 되니까


total = (n_list[start]+n_list[end])

if abs(total) < min_temp:
    min_temp= abs(total)
    result = n_list[start], n_list[end]
    # print(result)

if문에서 total을 활용할 때만 abs적용

'''

import sys
sys.setrecursionlimit(10**8)

n = int(input())

n_list = list(map(int, input().split()))

n_list.sort()

min_temp = 1e9 #0에 가장 가까운 값을 탐색

result = n_list[0], n_list[n-1]

def find_min(start, end):
    global min_temp
    global result

    if(start >= end):
        return result

    total = (n_list[start]+n_list[end])

    if abs(total) < min_temp:
        min_temp= abs(total)
        result = n_list[start], n_list[end]
        # print(result)
    
    if total < 0:
        start += 1
    elif total==0:
        return n_list[start], n_list[end]
    else:
        end -=1
    
    find_min(start,end)


find_min(0,n-1)
print(result[0], result[1])
        