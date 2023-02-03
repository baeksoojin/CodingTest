'''
노드의 개수 v, 간선의 개수 e
정점, 정점, cost를 e번 입력받을 때.

'''

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        parent[b] = a
    else:
        parent[a] =b

v,e = map(int, input().split())
parent = [0]*(v+1)

for i in range(1, v+1):
    parent[i] = i

edges = []
cost = 0

for _ in range(e):
    a,b,c = map(int, input().split())
    edges.append((c,a,b))

edges.sort() #핵심!

for eg in edges:
    c,a,b = eg
    if find_parent(parent,a) != find_parent(parent, b): #첫번째는 무조건 통과임
        union_parent(parent,a,b)
        cost += c
print(cost)

'''

입력예)

7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
답) 159

'''