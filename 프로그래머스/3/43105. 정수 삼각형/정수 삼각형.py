'''
왼쪽과 오른쪽 중에서 가장 큰 값으로 update하면 됨.

[i][j] 는 [i-1][j-1]과 [i-1][j] 중에서 큰 것을 선택해서 [i][j]와 더하기
'''


def solution(triangle):
    
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            # triangle의 i, j 위치의 숫자와 위에서 만들어진 숫자 중, 큰 값을 더하기
            
            ## 첫번째 숫자
            if j==0:
                triangle[i][j] += triangle[i-1][j]
            elif j==i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] = max(triangle[i-1][j-1],triangle[i-1][j]) + triangle[i][j]
        
    answer = 0
    for i in triangle[len(triangle)-1]:
        answer = i if answer < i else answer
        
    
    return answer