'''
문자열압축
idea) 
반복이 가능한 길이는 2부터 주어진 문자열을 2로 나눈 몫까지 가능하다. -> n

단위가 2일때)
다음 체크할 것의 범위가 문자열 최종길이를 넘어가는 경우 멈추기
while을 사용하자.

-----
1개단위는 반복되는걸로 취급하지 않는 것으로 보고 range를 2부터 돌렸는데 3번 testcase가 틀렸다.
보니까 1개단위도 반복으로 취급하는 것이였음...
제발 문제 잘 읽기^^

'''

import sys
input = sys.stdin.readline

s = input().strip()

max_unit = len(s)//2

result = len(s)
for unit in range(1, max_unit+1):
    same_cnt=1
    temp_string=''
    before = s[:unit]
    last_index = 0
    for i in range(unit,len(s), unit):
        if before == s[i:i+unit]:
            same_cnt+=1
        else:
            #이전과 연이어 같을 경우
            if same_cnt!=1:
                temp_string += str(same_cnt) +before
            else:
                temp_string += before
            same_cnt = 1
        before = s[i:i+unit]

    if same_cnt !=1:
        temp_string += str(same_cnt) + before
    else:
        temp_string += before
    
    result = min(result, len(temp_string))

print(result)

        
            

    