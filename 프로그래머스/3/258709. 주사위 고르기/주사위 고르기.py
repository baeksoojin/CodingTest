# 주사위 선택 = 252
# 2중 포문 -> 6의 10승
# 시간초과
# 

import itertools
from bisect import bisect_left

def solution(dice):
    answer = []
    
    m = len(dice)//2
    
    dic = {}
    
    # n개를 절반으로 나눈 m을 사용해서 주사위에서 나올 수 있는 수의 합을 각각 저장해야 시간복잡도를 6의 5승까지 낮춤
    dice_list = [i for i in range(len(dice))]
    split_dice_comb = list(map(list, itertools.combinations(dice_list, m))) # 절반씩 나누기
    # 주사위 선택
    for case1 in split_dice_comb:
        
        case2 = [i for i in range(len(dice)) if i not in case1]
        
        # case1, case2 둘다 적용
        choice_case = list(map(list, itertools.product(range(6), repeat = m ) ))# n개의 가능한 m개의 중복 수열 -> 만약 3개씩 주사위를 나눴을 때 0,0,0 뽑아도됨. 
        
        sums1 = []
        sums2 = []
        
        # case1의 조합에서 choice_case의 idnex를 뽑는다.
        
        
        for choice in choice_case: # 선택한 것들의 합을 저장
            
            sum1, sum2 = 0,0
            for dice_index, c in zip(case1, choice): # 주사위 조합은 고정. 무엇을 뽑는지만 달라짐
                sum1 += dice[dice_index][c]
            for dice_index, c in zip(case2, choice):
                sum2 += dice[dice_index][c]
            sums1.append(sum1)
            sums2.append(sum2)
        
        sums2.sort() # nlogn
            
        wins = sum(bisect_left(sums2, num) for num in sums1) 
        # sum2에서의 sum1의 num보다 작은 것의 개수 -> sum1이 더 큰 개수에 해당됨.
        dic[wins] = case1
    
    
    key = max(dic.keys())
    
    return [i+1 for i in dic[key]]