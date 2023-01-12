'''

add : 중복을 허용하지 않기에 set
remove : .remove를 사용한다(숫자를 입력)
check : s에 x가 있으면 1을 없으면 0을 출력한다 -> in 연산자 사용 => 해당 경우 결과를 출력
toggle : in을 통해서 있다면 remove를 수행. 없다면 add를 수행
all : {1,2,...,20}으로 기존의 집합을 변경한다.
empty : s를 공집합 {}으로 바꾼다.

'''

import sys
input = sys.stdin.readline

n = int(input())

s = set()

for _ in range(n):
    oper = input().split()

    if len(oper)==1:

        if oper[0].strip()=="all":
            s  = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
        else:
            s = set([])
    else:
        
        num = int(oper[1])
        oper = oper[0]
        
        if oper=="add":
            s.add(num)
        elif oper=="check":
            if num in s:
                print("1")
            else:
                print("0")
        elif oper=="remove":
            if num in s:
                s.remove(num)
            else:
                continue
        else:#toggle
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        
            