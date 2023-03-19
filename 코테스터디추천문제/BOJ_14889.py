'''
n/2를 조합합수를 사용해서 발생가능한 것을 다 뽑고 list에 저장
list에서 나온 수들로 만들 수 있는 능력치를 모두 더하고 list에 없는 수들의 집합 중에서 만들 수 있는 능력치를 모두 더해주기
이때 발생가능한 경우의 수중에서 가장 최솟값을 출력하기

# from itertools import combinations -> 백트래킹을 직접 -> combinations

'''

from itertools import combinations

n = int(input())

n_list = [i+1 for i in range(n)]
# print(n_list)# [1~8]

values = []

for i in range(n):
    values.append(list(map(int, input().split())))

teams = list()
teams += list(combinations(n_list,n//2)) 
min_teamvalue = 1e9

def calc_teamvalue(team):

    total=0

    for i in team:
        for j in team:
            total += values[i-1][j-1]
    
    return total

for team in teams:

    # print("team",team)
    diff_team = list(set(n_list) - set(team))
    # print("diff_team",diff_team)
    
    temp = abs(calc_teamvalue(team) - calc_teamvalue(diff_team))
    if temp < min_teamvalue:
        min_teamvalue = temp

print(min_teamvalue)
