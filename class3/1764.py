'''
듣도 못한 사람과 보도 못한 사람이 주어지면 둘다 속한 사람의 명단을 구하기
'''

n,m = map(int, input().split())

n_list = []
m_list = []

for i in range(n):
    n_list.append(input())

for i in range(m):
    m_list.append(input())

n_set = set(n_list)
m_set = set(m_list)
nm_set = n_set & m_set
print(len(nm_set))
nm_list = sorted(list(nm_set))

for i in range(len(nm_list)):
    print(nm_list[i])

