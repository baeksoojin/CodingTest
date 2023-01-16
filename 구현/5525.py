'''

1시시작!

문제
IOI +OI*(n) 문자열이 몇개나 포함되어있는지 count함.
만약에 IOIOI(길이 5)를 찾는데 IOIOOO라는 총 6개의 문장을 살핀다면(6-5+1 => 총 2번)번만 살필 수 있음 -> for문의 조건

idea)
IOI를 디폴트로하고 n을 입력받으면 OI를 n번 string에 더해주고 계산
-> for문을 돌게되는데 n*m = > 1000000*1000000 -> 당연히 10^7을 넘겨서 시간복잡도가 1초를 넘겨서 시간초과가 될 것임
-------
IOI 단위(3개씩)로 자르면서 index를 증가(count는 0부터시작)
- 있다면 2를 증가시키고 IOI가 반복되는지 체크한 후에 반복된다면 count를 1증가시킴. 반복횟수가 곧 n의 수가 됨, 없다면 1(count값을 0으로 만들기)
- 중요한 점 : index가 IOI를 발견하면 2 증가되고 또 발견되면 또 2가 증가 됨.
그래서 만약에 n=2일때(IOIOI를 찾는것) IOIOIOI일때 [ IOI -> {IOI (1번)] -> IOI} ()세트와 {}세트 총 2번이 증가되어야함
그래서 첫번째 ()에서 count가 1이 된 이후 count를 다시 0으로(count -=1) 만들고 5번째 index부터 IOI가 또 있어서 count가 1이 되어야함.
=> count==n이 되었을 때 count -=1을 해줘야한다.

'''
# 시간초과 코드
'''
import sys
input = sys.stdin.readline

n = int(input())
n_list = 'IOI'
for i in range(1,n):
    n_list +="OI"

m = int(input())
m_list = input().strip()

count=0

for i in range(len(m_list)):
    if m_list[i:i+len(n_list)] == n_list:
        count +=1

print(count)

'''

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
p = input().strip()

i, result, count = 0,0,0

while(i < m-1 ):
    print(p[i:i+3])
    if p[i:i+3]=="IOI":
        count +=1
        i += 2
        if count == n:
            count -=1
            result+=1
    else:
        i+=1
        count = 0


print(result)