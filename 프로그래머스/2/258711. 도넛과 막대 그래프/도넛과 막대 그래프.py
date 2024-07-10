
# 생성한 정점은 들어오는 간선이 0개이고 나가는 정점이 2개 이상이다.
# 막대모양은 나가는 간선이 0개이고 들어오는 간선이 1개인 노드의 개수이다.
# 8자모양 그래프는 나가는 (중간연결)부분이 2개이고 들어오는 부분이 2개인 노드의 개수이다.
# 생성한 정점의 나가는 간선 수에서 막대모양과 8자 모양을 밴 경우

def solution(edges):
    answer = [0,0,0,0]
    
    in_out = dict()
    
    for edge in edges:
        # 나가는 것, 들어오는 것
        a, b = edge[0], edge[1]
        if a not in in_out:
            in_out[a] = [0, 0]
        if b not in in_out:
            in_out[b] = [0, 0]
            
        in_out[a][0] += 1
        in_out[b][1] += 1
        
    
    bridge_count = 0
    for key, value in in_out.items():
        
        if value[0] >= 2 and value[1] == 0: # 나가는 간선이 2개이상이고 들어오는 것은 answer[0]의 값
            answer[0] = key
            bridge_count = value[0]
        elif value[0]==0 and value[1] >0: # 막대모양
            answer[2] +=1
        elif value[0] >=2 and value[1] >= 2:
            answer[3] +=1
        
    answer[1] = bridge_count - answer[3] - answer[2]
    
    return answer