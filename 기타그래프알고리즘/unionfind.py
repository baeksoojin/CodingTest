# 2. 연산단계 중 find
def find_parent(parent, x):
    
    # root node 판별
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x]) #compression
    return parent[x]

# 2. 연산단계 중 union
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent,b)

    #루트노드중 큰 것을 작은 것(더 부모쪽)으로 변경
    if a<b:
        parent[b] =a
    else:
        parent[a] =b

## 1. 초기세팅

v,e = map(int, input().split()) # node v개 , union(간선) e개
parent = [0]*(v+1)

# parent를 자기자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 2. 연산 수행
for _ in range(e):
    a,b = map(int, input().split())
    union_parent(parent,a,b)

# 3. root노드 최종 업데이트
for i in range(1, v+1):
    print(find_parent(parent, i), end=" ")
print()

# 부모 테이블 내용 출력
for i in range(1, v+1):
    print(parent[i], end=' ')