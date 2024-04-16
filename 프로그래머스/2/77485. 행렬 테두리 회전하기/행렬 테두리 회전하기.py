'''
1시 9분 시작
1. 회전 방향 순서대로 배열에 담기 -> rotate(queue사용) -> 다시 방향 순서대로 넣기
1번 진행 과정에서, 가장 작은 것을 뽑기

'''

from collections import deque

def solution(rows, columns, queries):
    answer = []
    
    arr = [[0]*columns for _ in range(rows)]
    
    # 행렬 초기화
    num = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = num
            num+=1
    # queries 개수만큼 rotate적용
    queue = deque()
    
    for q in queries:
        queue.clear()
        
        start_i = q[0]-1
        start_j = q[1]-1
        end_i = q[2]-1
        end_j = q[3]-1
        
    
        queue.extend(arr[start_i][start_j:end_j+1]) # 상

        queue.extend([row[end_j] for row in arr[start_i+1: end_i]]) # 우
    
        queue.extend(arr[end_i][start_j:end_j+1][::-1]) # 하
      
        queue.extend([row[start_j] for row in arr[start_i+1:end_i][::-1]]) # 좌
        
        
        answer.append(min(list(queue)))
        queue.rotate(1)
        
        for i in range(start_j, end_j+1):
            arr[start_i][i] = queue.popleft()
        for i in range(start_i+1, end_i):
            arr[i][end_j] = queue.popleft()
        for i in range(end_j, start_j, -1):
            arr[end_i][i] = queue.popleft()
        for i in range(end_i, start_i, -1):
            arr[i][start_j] = queue.popleft()
        
    
    return answer