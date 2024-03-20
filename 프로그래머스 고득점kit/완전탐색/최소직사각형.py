'''
3월 19일 8시54분~ 9t시 14분

1. 가로, 세로 중에서 가장 큰 값을 가지는 것을 선택 -> 그게 가로인지,세로인지도 확인해야함.
2. 가장 큰 값의 범위에 각 지갑의 모든 면이 들어가는것이기에 각 지갑마다 큰 값을 다른 범위의 기준이 되도록하며, 
해당 값을 탐색하며 가장 큰 값을 선택(단, 큰 값을 가졌던 index는 제거한다)
'''


def solution(sizes):

    answer = 0
    
    # 가장 큰 값을 가지는 면과 값을 선택
    type = 0 # 0일때는 가로, 1일때는 세로
    max_index = 0 # 가장 큰 길이를 가지는 면에 해당하는 지갑의 index
    max_size1 = 0
    for i in range(len(sizes)):
        for j in range(len(sizes[0])):
            
            if sizes[i][j] > max_size1:
                max_index = i
                max_size1 = sizes[i][j] 
                type = j
    
    max_size2 = sizes[max_index][type-1]

    sizes.pop(max_index) # 가장 큰 값을 지갑은 탐색할 필요가 없음
    
    for i in range(len(sizes)):
        if min(sizes[i]) > max_size2:
            print(min(sizes[i]))
            max_size2 = min(sizes[i])

    return max_size1*max_size2