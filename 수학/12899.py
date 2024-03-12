def solution(n):
    answer = ''
    
    '''
    1,2,4로 조합하여 만들 수 있는 숫자
    몫과 나머지를 활용해야하는 문제.
    몫의 몫의 몫의,,,,몫이 0으로 떨어질때까지 반복하며 나머지를 활용해서 각 자릿수의 수를 구해주면 됨.
    단, 각 몫에서 -1을 해주고 시작. (python은 0부터 시작하니까)
    '''
    
    answer = []
    
    while n:
        n-=1
        answer.append('124'[n%3])
        n//=3
        
    #print(answer)
    return ''.join(answer[::-1])
       