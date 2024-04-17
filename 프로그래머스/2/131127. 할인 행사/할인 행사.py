'''
1시 50분 시작

'''

import copy

def solution(want, number, discount):
    answer = 0
    
    dict_want = dict()
    for i in range(len(want)):
        dict_want[want[i]] = i
    want_list = set(want)
    
    
    for i in range(len(discount)-9):
        
        temp_number = copy.deepcopy(number)
        temp_discount_list = discount[i:i+10]
        flag = True
        for d in temp_discount_list:
            if d in want_list:
                temp_number[dict_want[d]] -=1
            else:
                flag = False
                break
        if flag==True:
            flag2 = True
            for i in temp_number:
                if i!=0:
                    flag2= False
                    break
            if flag2 == False:
                continue
            else:
                answer+=1
            
            
    return answer