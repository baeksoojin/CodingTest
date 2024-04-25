'''
solve 2
'''

def solution(n, lost, reserve):
    answer = 0
    
    reserve_set = set(reserve)
    lost_set = set(lost)
    same_set = reserve_set & lost_set
    
    
    reserve = list(reserve_set - same_set)
    lost_set = lost_set - same_set
    
    
    for i in range(len(reserve)):
        
        before = reserve[i] -1 
        after = reserve[i]+1
        
        if before in lost_set:
            lost_set.remove(before)
        elif after in lost_set:
            lost_set.remove(after)
            
        
    return n-len(lost_set)