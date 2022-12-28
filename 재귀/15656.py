# 같은수를 여러번 선택가능 -> 순열

n,m = map(int, input().split())
n_list = sorted(list(map(int, input().split())), reverse=False)

result=[0]*10

def recursion(n,m,level):

    if m==level:
        for i in range(m):
            print(result[i], end=" ")
        print("")
        return

    for i in range(n):
       result[level] = n_list[i]
       recursion(n,m,level+1)

recursion(n,m,0)