
'''
6시 57분 시작 -> 7시 26분 완료.

9개의 영역으로 나누며 영역을 좁게 만들어줘야해서 재귀를 사용하는 분할정복 문제

'''

import sys
input = sys.stdin.readline

n = int(input())

paper = []

for i in range(n):
    paper.append(list(map(int, input().split())))

result_count = [0]*3

def check(a,b,size):

    diff_check =[False]*3

    if size==1:
        # print(a,b)
        if paper[a][b]==-1:
            result_count[0]+=1
        elif paper[a][b]==0:
            result_count[1]+=1
        else:
            result_count[2]+=1
        return
    else:
        for i in range(a,a+size):
            for j in range(b,b+size):
                if paper[i][j]==-1:
                    diff_check[0]=True
                elif paper[i][j]==0:
                    diff_check[1]=True
                else:
                    diff_check[2]=True
        # print(a,b,size,diff_check)
        if diff_check.count(True)!=1:
            check(a,b,size//3)
            check(a,b+size//3,size//3)
            check(a,b+(size//3)*2,size//3)
            check(a+size//3,b+0,size//3)
            check(a+size//3,b+size//3,size//3)
            check(a+size//3,b+2*(size//3),size//3)
            check(a+(size//3)*2,b+0,size//3)
            check(a+(size//3)*2,b+(size//3),size//3)
            check(a+(size//3)*2,b+(size//3)*2,size//3)
        else:
            for i in range(3):
                if diff_check[i]==True:
                    result_count[i]+=1
            return
            
        

check(0,0,n)

for i in result_count:
    print(i)