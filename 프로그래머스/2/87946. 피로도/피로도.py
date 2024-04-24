'''
solve 2
5시~
'''

import itertools

def solution(k, dungeons):

    answer_set = set()
    
    max_kind = len(dungeons)
    index_list = []
    for i in range(max_kind):
        index_list.append(i)
        
    
    permutation_list = list(itertools.permutations(index_list, max_kind))
    max_count = -1
    for p in permutation_list:
        index_list = list(map(int, p))
        count= 0 
        k_temp = k
        for i in index_list:
            if k_temp >= dungeons[i][0]:
                k_temp -= dungeons[i][1]
                count+=1
                continue
            break
        if count> max_count:
            max_count = count
    print(max_count)
    return max_count