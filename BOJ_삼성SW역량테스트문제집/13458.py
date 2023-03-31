'''
시험장을 돌면서 총감독관 1명이 체크가능한 B수를 각 방에서 빼고 남은 인원을 부감독관이 처리

'''

n = int(input())
people = list(map(int, input().split()))

b,c = map(int, input().split())

result=0
for p in people:
    
    # 총감독관을 배치
    diff = p - b
    result+=1

    cnt=0
    # 부감독관을 배치
    if diff<=0:
        continue
    if diff % c ==0:
        result+=diff//c
    else:
        result+=diff//c+1
print(result)

'''
반례

input
8
5 10 30 235 1 23 24 101
10 3
ouput
127
ans
131

부감독관 배치하지 않을 조건에서 감독관한명이 처리가능한 수를 뺀 diff => - 일때를 고려하지 않음

before)
if diff=0:
    continue 

after)
if diff<=0:
    continue  

'''