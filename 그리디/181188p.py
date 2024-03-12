'''

최소한으로 미사일을 발생해서 모든 미사일을 요격

발사한 미사일은 x축에 평행한 직선. (s,e)구간에서 폭격
관통 요격 : x좌표에 걸쳐있는 모든 폭격 미사일을 관통
폭격 미사일은 s와 e에서 발사하는 요격 미사일로 요격 불가능.(그 사이에서 제거가 가능.포함X). 
---

그리디? 
끝나는 시간이 빠른 것을 발견. count+1 -> 선택된 개구간의 s에 다른 것이 속해있다면 그것은 counting에서 pass
'''


def solution(targets):
    answer = 0
    
    targets.sort(key = lambda x: x[1])

    
    current_s = current_e = 0
    
    for target in targets:
        if current_e <= target[0]:

            answer +=1
            current_e = target[1]
            
    
    return answer