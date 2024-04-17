'''
n^2 배열 자르기
1시 10분 시작

'''


def solution(n, left, right):
    answer = []
    
    current = left
    
    while True:
        if current > right:
            return answer
        
        q = (current)//n
        r = (current)%n
        
        if (q) < r:
            answer.append(r+1)
        else:
            answer.append(q+1)
            
        current+=1
            
    print(answer)
    
    return answer
     
    