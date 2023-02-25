'''
에디터

12시 48분시작

처음에 위치한 원소만을 뽑을 수 있기에 popleft()를 사용해야함.
처음에 위치하게 하기 위해서 왼쪽으로 이동 혹은 오른쪽으로 이동하도록 연산을 수행해야함.

왼쪽으로 한칸 이동하는 경우 -> 가장 앞의 것을 뽑아서 새로운 리스트의 맨 마지막으로 넣고 그 이전을 직전 배열로 함
오른쪽으로 한칸 이동 -> 가장 뒤에 있던 것을 뽑아서 다른 리스트의 맨 처음에 넣고 나머지 직전 배열에 있던 것을 그 뒤로 붙임

뽑아내기 위해서 최소가 되려면 원소의 위치를 찾아서 왼쪽에 가짜우면 왼쪽으로 이동하는 연산을 수행하고
오른쪽에 가까우면 오른쪽으로 가는 연산을 진행한다.


이동하는 연산의최솟값!

왼쪽으로 이동 -> deque.rotate(-1)
오른쪽으로 이동 -> deque.rotate(1)
위치하는 index 찾기 -> deque.index(n)

'''

from collections import deque

n,m = map(int, input().split())

m_list = list(map(int, input().split()))
n_list = deque([])
for i in range(1,n+1):
    n_list.append(i)

cnt = 0
# logic
for target in m_list:

    while(True):
        if n_list[0] == target:
            n_list.popleft()
            break
        else:
            #연산횟수 카운팅
            if n_list.index(target)<=len(n_list)//2:
                n_list.rotate(-1)
                cnt+=1
            else:
                n_list.rotate(1)
                cnt+=1

print(cnt)   
    
