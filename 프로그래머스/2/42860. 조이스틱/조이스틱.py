def solution(name):
    answer = 0
    
    # 위아래 조이스틱

    
    min_temp = len(name)-1
    
    while name[min_temp] == 'A' and min_temp >=0:
        min_temp -=1
    if min_temp < 0 : # 모두 A로 구성된 경우
        return answer
    
    for i, value in enumerate(name):
        answer+= min(1 + ord('Z') - ord(value), ord(value) - ord('A'))
        
        next = i+1
        while next < len(name) and name[next] =='A':
            next+=1
        # 기존의 위치와 변경된 위치 중 적합한 꺾이는 곳을 찾는 것
        
        min_temp = min(min_temp, 2*i + len(name) - next, 2 * (len(name)- next) + i)
        
    answer+=min_temp
    
    return answer