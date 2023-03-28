'''
bfs를 사용해서 최소 count를 체크한다.
'''

from collections import deque 

def solution(begin, target, words):
    answer = 0
    
    queue = deque([])
    queue.append((begin,0))
    
    word_len = len(begin)
    visited = [False]*(len(words))
    
    while(queue):
        
        #pop
        current, cnt = queue.popleft()
        print(current)
        
        if current == target:
            print("result",cnt)
            answer = cnt
            return answer
        
        # 다음으로 올 수 있는 것들을 모두 탐색
        for word in words:
            # 한개의 알파벳만 다른게 있고 방문하지 않았더라면 모두 queue에 저장
            same_count = 0
            for i in range(word_len):
                if current[i] == word[i]:
                    same_count+=1
            word_index = words.index(word)
            if same_count==word_len-1 and visited[word_index]==False:
                # queue에 저장
                queue.append((word,cnt+1))
                #visited체크
                visited[word_index]=True
            
                
    return answer
        
    
    
