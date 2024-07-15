'''
아래에 있는 주사위의 웃면 = 위의 주사위의 아랫면
단, 1번은 맘대로 놓을 수 있음
위, 아래를 고정하고 나머지 면에서 가장 큰 수를 한 면에 배치 -> 그 합을 구하면 정답
'''

# 6가지 경우의 수 -> 1부터 아래에 두면 위는 자동 결정. 2번의 아래도 자동 결정됨.

# 주사위의 아랫면이 결정됐다면 -> 그 index를 찾고 mapping을 통해 윗면의 index를 find
# 0 <-> 5 / 1 <-> 3 / 2 <-> 4에 각각 대응됨
mapping = [5,3,4,1,2,0]

def find_up_value(bottom, dice):

    bottom_index = dice.index(bottom)
    upper_index = mapping[bottom_index]
    return (bottom_index,upper_index)

n = int(input())
base_case = 6

dices = []
for i in range(n):
    dices.append(list(map(int, input().split())))

result = 0
for start in range(1,base_case+1): # 가장 아래 밑면을 고르는 경우

    current_max =0
    bottom = start

    for j in range(n):
        dice = dices[j]
        b_index, u_index = find_up_value(bottom, dice)
        temp_max = 0
        for k in range(6):
            if k != b_index  and k!=u_index:
                temp_max = max(temp_max, dice[k])
        current_max += temp_max
        bottom = dice[u_index]
    result = max(result, current_max)

print(result)

        


    

    



