import itertools

def solution(k, dungeons):
    answer = -1
    
    # 조합으로 탐색
    size = len(dungeons)
    case = []
    for i in range(size):
        case.append(i)
    case_list = list(itertools.permutations(case, size))
    
    answer = []
    for i in range(len(case_list)):
        temp = case_list[i]
        count=0
        k_temp = k
        for j in range(size):
            if dungeons[temp[j]][0] <= k_temp:
                count+=1
                k_temp = k_temp - dungeons[temp[j]][1]
        answer.append(count)
                
    return max(answer)