'''
최대한 겹쳐야하기에 시작지점에서 끝지점까지 겹치는것을 체크
'''


def solution(routes):
    answer = 0
    
    routes.sort(key = lambda x: x[1])
    current_end = routes[0][1]
    routes.pop(0)
    answer+=1
    for start, end in routes:
        if current_end >= start:
            continue
        else:
            current_end = end
            answer+=1
    
    return answer