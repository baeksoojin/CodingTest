'''
<조건>
모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현이 가능하다.
자연수를 넷 혹은 그 이하의 제곱수의 합으로 나타내라는 것.
n을 최소 개수의 제곱수의 합으로 표현하는 컴퓨터 프로그램 작성 

시간이 0.5초 주어짐( 5*10^6 까지 가능)

idea)
---
일단은 50,000까지 만들 수 있느 최소의 값을 채우기 =>(19분 소요) 하지만 시간이 너무 오래걸림
----
변경해서 최대로 만들수 있는 제곱근에서 하나씩 앞으로 가면(그리디) 그 수가 곧 최소 개수가 되지 않을까 기대함. -> (21분까지)
=> testcase는 모두 정답이지만,..틀렸습니다가 3%에서 나오는걸로봐서 틀린 로직같음.

----
가장 가까운 제곱근일때 정답이라고생각했지만 그렇지 않은 경우가 있을 수 있음을 알아냄(12)
-----

이후 코드 변경 후 시간초과...... -> pypy는 되는데 python은 안 됨

'''

n = int(input())
INF = int(1e10)
count =[INF]*(50001)
count[1] = 1

for i in range(1,n+1):

    temp = int(i**(0.5))
    # print(i,temp)
    if temp**(2) == i:#제곱근일때
        # print("제곱근일때")
        count[i] = 1
    else:
        for j in range(1,temp+1):
            check = j**2
            if 2<=count[check]+count[i-check]<=3:
                count[i] = min(count[i],count[check]+count[i-check])
                if count[i]==2:
                    break

# print(count[:n+1])
if count[i]==INF:
    print("4")
else:
    print(count[n])



