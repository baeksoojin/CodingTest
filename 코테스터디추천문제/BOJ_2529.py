'''
3시 10분 시작 [12분 over]

< 를 기준으로 앞에는 더 작은 수가 와야하고 뒤에는 큰 수가 와야함.

최댓값을 찾으려면 앞에나오는 수가 남은 수중에서 가장 큰 수가 되어야함.

여러가지 경우의 수를 모두 체크하는 과정 중에서 수의 크기를 비교해야하는 문제이니까 백트래킹이랑 그리디를 적용

3시 52분에 끝
=> level 이 0이아닐때는 연산자 비교를 하지 않는 것을 숫자 0일때는 비교하지 않음. 혹은 9일때는 비교하지 않음으로 작성해서 로직에러
-> 숫자로 비교하면 두번째 자리에도 9혹은 0일때도 적용돼서 첫번째만 연산자 비교를 하지 않으려고 짠 코드의 의도가 달라짐
=> level이 0일때만 패스하게끔작성하도록함....^^




'''

n = int(input())

n_list = list(input().split())
length = n+1

min_list = [0]*(length)
min_visitied = [False]*(11)
min_cnt = 0

def find_min(level):

    global min_cnt

    if level==length:
        for i in range(level):
            print(min_list[i], end="")
        min_cnt+=1
        return

    for i in range(0,10):
        if min_visitied[i]==False:
            if level!=0:
                oper = n_list[level-1]
                if oper==">":
                    if min_list[level-1] <= i:
                        continue
                if oper=="<":
                    if min_list[level-1] >= i:
                        continue
            min_list[level] = i
            min_visitied[i] = True
            find_min(level+1)
            if min_cnt==1:
                return
            min_visitied[i] = False




max_list = [0]*(length)
max_visitied = [False]*(11)
max_cnt = 0


def find_max(level):

    global max_cnt

    if level==length:
        for i in range(level):
            print(max_list[i],end='')
        max_cnt+=1
        return

    for i in range(9,-1,-1):
        if max_visitied[i]==False:
            if level!=0:
                oper = n_list[level-1]
                if oper==">":
                    if max_list[level-1] <= i:
                        continue
                if oper=="<":
                    if max_list[level-1] >= i:
                        continue
            max_list[level] = i
            max_visitied[i] = True
            find_max(level+1)
            if max_cnt==1:
                return
            max_visitied[i] = False


find_max(0)
print()
find_min(0)
print()

  