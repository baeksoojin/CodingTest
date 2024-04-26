'''
최소 신장 트리를 활용한다.
costs를 돌면서 하나씩 접근. (가장 적은 것부터 선택)
그리디 알고리즘 -> 가장 적은 간선부터 선택 ->> 이때, 그 간선이 사이클을 만들지 않아야한다. 무방향일때 가능.
'''

def find_parent(parent, node):
    
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])
    return parent[node]
    
    
def union(parent,a,b): # 작은 노드를 부모로 가지는 것에 합치기
    
    a_parent = find_parent(parent, a)
    b_parent = find_parent(parent, b)
    if a_parent < b_parent:
        parent[b_parent] = a_parent
    else:
        parent[a_parent] = b_parent


def solution(n, costs):
    sorted_cost = []
    
    # 1번 cost를 기준으로 정렬한다.
    for cost in costs:
        
        sorted_cost.append([cost[2], cost[0], cost[1]])
        
    sorted_cost.sort()
        
    # parent를 자기자신으로 초기화
    parent = []
    for i in range(n):
        parent.append(i)
    
    
    min_cost = 0
    # costs를 돌면서 적은 것부터 꺼낸다.
    for cost in sorted_cost:
        c,a,b = cost[0], cost[1], cost[2]
        # cycle 체크
        # 1. cycle이 생긴다 -> continue
        if find_parent(parent, a) == find_parent(parent, b):
            continue
        else: # 2. cycle이 생기지 않는다. -> 연결해준다. union 
            union(parent, a, b)
            min_cost += c
        

    return min_cost