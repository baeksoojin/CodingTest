'''
값마다 for문을 다 돌리면서 적은 것을 체크하기엔 시간이 너무 비효율적으로 사용되니까 Index를 활용해야할 것 같음

주의할점은 같은 값이 여러번 있을 수 있다는 것.

dictionary를 사용해서 이미 앞에서 나온 수에 대해서는 key값이 있다면 어떠한 연산도 진행하지 않도록 함.
dictionary에 key에 n값을 넣고 각 수에 해당하는 결과값을 value로 넣음

'''

import sys
input = sys.stdin.readline

n = int(input().strip())
n_list = list(map(int,input().split()))

sorted_list = sorted(n_list)

dic = dict()
count=0

for i in range(0,n):

    key = str(sorted_list[i])
    if i==0:
        dic[key] = 0
        count+=1
    else:
        if not key in dic.keys():
            dic[key] = count
            count+=1
        else:
            continue

for n in n_list:
    print(dic[str(n)], end=" ")