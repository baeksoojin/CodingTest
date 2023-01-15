'''

7시 40분 시작 -> 8시 2분 완료.

4등분으로 나눠서 체크하는 과정을 반복하는 재귀를 활용한 분할정복 문제로 판단됨
괄호를 어떻게 체크하냐가 관건.

깊이를 하나 더 드어갈때마다 (를 붙여주고 시작해야함. (다만 사이즈가 1일때는 괄호를 붙이지 않음)
4군데를 다 간다음에 괄호 )를 붙여줘야함. -> 4개의 재귀 다음에 )를 붙여주기

'''

import sys
input = sys.stdin.readline

n = int(input())

tree = []

for i in range(n):
    temp = input().strip()
    tree.append(list(map(lambda x : int(x),temp)))


result = []


def check(a,b,size):

    is_in =[False]*2

    
    if size==1:
        result.append(tree[a][b])
        return
    else:
        for i in range(a, a+size):
            for j in range(b, b+size):
                if tree[i][j]==0:
                    is_in[0]=True
                else:
                    is_in[1]=True
        #print(a,b,size,is_in)
        if is_in.count(True)>1:
            #재귀 
            result.append("(")
            check(a,b,size//2)
            check(a,b+size//2,size//2)
            check(a+size//2, b, size//2)
            check(a+size//2,b+size//2, size//2)
            result.append(")")
        else:
            for i in range(2):
                if is_in[i]==True:
                    result.append(i)
            return
check(0,0,n)
# print(result)
for i in result:
    print(i,end="")