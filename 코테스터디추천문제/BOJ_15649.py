'''
3시16분 30분 이내로 풀어야함

사전 순으로 증가하는 순서를 출력해야한다.
'''


n,m = map(int,input().split())

result = [0]*(n+1)
visited = [False]*(n+1)
def recursive(level):
    if level==m:
        for i in range(m):
            print(result[i], end=" ")
        print()
        return

    for i in range(1,n+1):
        if visited[i]==False:
            visited[i]=True
            result[level] = i
            recursive(level+1)
            visited[i]=False            


recursive(0)