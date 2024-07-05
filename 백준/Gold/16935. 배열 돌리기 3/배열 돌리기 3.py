n,m,r = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

r_list = list(map(int, input().split()))


def apply_oper_1(graph):
    for i in range(n//2):
        for j in range(m):
            graph[i][j], graph[n-i-1][j] = graph[n-i-1][j],  graph[i][j]
    
    return graph

def apply_oper_2(graph):
   
    for i in range(n):
        for j in range(m//2):
            graph[i][j], graph[i][m-j-1] = graph[i][m-j-1],  graph[i][j]

    return graph

def apply_oper_3(graph):
   
    graph = list(map(list,zip(*graph[::-1])))

    return graph



def apply_oper_4(graph):

    for i in range(3):
        graph = list(map(list,zip(*graph[::-1])))

    return graph

def apply_oper_5(graph):
   
    temp = [[0]*m for _ in range(n)]

    # 4 -> 1
    for i in range(n//2):
        for j in range(m//2):
            temp[i][j] = graph[n//2+i][j]

    # 1-> 2
    for i in range(n//2):
        for j in range(m//2):
            temp[i][j+ m//2] = graph[i][j]
    
    # 2 -> 3
    for i in range(n//2):
        for j in range(m//2):
            temp[i+n//2][j+m//2] = graph[i][j+m//2]
    
    for i in range(n//2):
        for j in range(m//2):
            temp[i+n//2][j] = graph[i+n//2][j+m//2]
        
   
    return temp

def apply_oper_6(graph):

    temp = [[0]*m for _ in range(n)]
    
     #1 - 4
    for i in range(n//2):
        for j in range(m//2):
            temp[n//2+i][j] = graph[i][j]

    # 4 -> 3
    for i in range(n//2):
        for j in range(m//2):
            temp[i+n//2][j + m//2] = graph[i+n//2][j]
    
    # 3 -> 2
    for i in range(n//2):
        for j in range(m//2):
            temp[i][j+m//2] = graph[i+n//2][j+m//2]
    
     # 2 -> 1
    for i in range(n//2):
        for j in range(m//2):
            temp[i][j] = graph[i][j+m//2]


    return temp
for oper in r_list:

    if oper==1:
        graph = apply_oper_1(graph)
    elif oper==2:
        graph = apply_oper_2(graph)
    elif oper==3:
        graph = apply_oper_3(graph)
        n,m = len(graph), len(graph[0])
    elif oper==4:
        graph = apply_oper_4(graph)
        n,m = len(graph), len(graph[0])
    elif oper==5:
        graph = apply_oper_5(graph)
    else:
        graph = apply_oper_6(graph)

for i in range(len(graph)):
    print(" ".join(map(str, graph[i])))