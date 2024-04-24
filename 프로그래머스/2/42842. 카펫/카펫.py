'''
solve 2
'''
import math

def solution(brown, yellow):
    answer = []
    
    # 1. 가로 세로가 될 수 있는 조합을 탐색 -> temp_list
    
    temp_list = []
    
    for i in range(1, int(math.sqrt(yellow))+1):
        if yellow % i ==0:
            temp_list.append((i,yellow // i))
    # 가로*2 + 세로 *2 +4한게 brown을 만족하면 return
    for w,h in temp_list:
        if w*2 + h*2 + 4 == brown:
            answer = [w+2,h+2] if w>h else [h+2,w+2]
    
    return answer