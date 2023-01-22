'''
인접한 것끼리의 최대 높이차가 결국 최소가 되어야함.

10^5*10*5를 할 수는 없으니까 for문으로 완전탐색을 하면 안 됨.
다른 규칙이 있다는 것

-----
2,4,5,7,9가 있을 때처럼 정렬이 되면 인접한 것들끼리의 최대 높이차가(정렬하기 전의 경우를 모두 포함했을 때) 최소(정렬이후)인 경우중에서 가장 큰 차이값이 될텐데 다만 여기서의 정답은 7이다.
처음과 끝을 고려해야함.. 따라서 그냥 정렬하면 안 됨.
어떻게 해야하는지 모르겠음! 그래서 그냥 testcase랑 비교....
testcase분석)
=> 2,5,9,7,4인 경우에 최대 높이차가 최소인 경우에 해당함.
어떻게 해당 결과가 나왔는지??...? 규칙을 보니까 뭔가 가장 앞에 가장 작은 수 다음수를 맨 뒤에 그리고 가장 앞에서 두번째에 그 다음의 수 그리고 뒤에서 두번째에 그 다음수를 저장하는 것처럼 들어감.

위의 가정이 맞는지 체크
10 10 11 11 12 12 13일때
10 11 12 
12 11 10
사이에 13

=> 결과는 1이 나와야함.

----
idea)
우선 정렬
가운데는 항상 가장 큰 수
cnt 짝수) 왼쪽 배열에 앞에서부터 집어넣음
cnt 홀수) 오른쪽 배열에 앞에서부터 집어넣고 -> 가장 마지막에만 reverse하기

정렬하고 문제의 조건을 맞춰서 다시 순서를 변경한 것중에 가장 큰 값을 찾는것으로 그리디

----
느낀점
완탐이 안 되면 규칙이있다는 건데 그 규칙을 문제에 주어진 예시를 보고 알아보면 은근 쉽게 풀 수 있음..!!
이게 맞다고? 하는데 맞음....^^

'''

import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    sorted_list = sorted(list(map(int, input().split())),reverse=False)
    temp1=[]
    temp2=[]
    for j in range(len(sorted_list)-1):#가장 큰 값 제외
        if j%2==0:
            temp1.append(sorted_list[j])
        else:#3일때 뒤의 배열에 들어가야하고 index는 1이 되어야함.
            temp2.append(sorted_list[j])
    temp1.append(sorted_list[-1])
    temp2.reverse()
    temp1.extend(temp2)
    max = 0
    for j in range(0,len(temp1)-1):
        if max < abs(temp1[j+1] - temp1[j] ):
            max = abs(temp1[j+1] - temp1[j] )
    print(max)

        
    
    