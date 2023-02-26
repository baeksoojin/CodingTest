def solution(clothes):
    
    # dict에 종류별로 보관. 해당 종류로 만들 수 있는 옷의 개수+1
    
    dict = {}
    
    for cloth, type in clothes:
        
        if type in dict.keys():
            dict[type]+=1
        else:
            dict[type] =1
    
    total = 1
    print(dict)
    for type in dict.keys():
        total = total*(dict[type]+1)
        
    return total-1
            