'''
2시 13분 시작 -> 목표 실버3[20분] 27분 끝.
dictionary를 사용해서 카테고리별로 아이템을 정리하고 카테고리는 각각 사용하거나 사용하지 않거나 총 2가지 경우를 가진다.

만약에 headgear에 hat, turban이 존재
heager에서 1개를 무조건 사용하거나 heager에서 1개도 사용하지 않거나의 경우임
heager에서 1개를 무족너 사용하는 경우는 heagear에 들은 "item의 개수"이다. 아무것도 사용하지 않는 경우는 "1개임"

이때 eyewear가 1개 있다면 
eyewear에서 1개를 사용하는 경우(eyewear 아이템의 개수)
아무것도 사용하지 않는 경우(1개)

종류별 개수를 서로 곱하면 result?

------

카테고리별로 각 경우의 수를 구하고 서로 곱한 값에서 -1을 해줘야함(모두 선택하지 않는 경우일때에에 해당함)

'''

t = int(input())

for _ in range(t):
    n = int(input())
    dic = dict()
    for i in range(n):
        item, key = input().split()
        
        if key in dic.keys():
            #이미 카테고리가 존재할때
            before = dic[key]
            dic[key] = [item]+before
        else:
            dic[key] = [item]
    case = 1
    for key,values in dic.items():
        temp = 1 + len(values)# 아무것도 선택하지 않는 경우의 수 + item들 중에서 1개를 선택하는 경우의 수
        case = case*temp
    case -=1# 모든 카테고리를 전혀 고르지 않은 경우.
    print(case)
