'''
0과 r2사이의 값에서 x,y의 숫자가 존재가능.
이때, x^2 + y^2이 r1과 r2의 사이에 존재해야함.(포함가능)


'''

import math
def solution(r1, r2):
    answer = 0
    
    for i in range(0, r2):
            answer += int(math.sqrt(r2**2 - i**2)) - int(math.sqrt(max(r1**2 - i**2-1, 0)))
                
    return answer*4