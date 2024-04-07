'''
list에 있는 값에서 최솟값 2개를 뽑고 섞은다음 디시 저장.
가장 작은 값의 스코빌지수가 k값 이상일때 그만.
-> sort를 계속하면서 뽑을 수 없으니 heap을 사용해서 가장 작은 것을 뽑아내야함.

3시 20분 6시10분 시작
'''

import heapq

def solution(scoville, K):
    
    mix_count = 0
    scoville_heap=[]
    
    for i in scoville:
        heapq.heappush(scoville_heap, i)
        
    
    while scoville_heap:  # 더해지다가 1개또는 0개가 남은 경우, 더이상 비교할 숫자가 없을 때 종료
        
        
       # 중간에 합치면서도 스코빌 지수를 모두 넘지 않은 경우
        if len(scoville_heap)==1: # 합치고 보니, 더이상 합칠 대상이 없고 마지막 1개만 남은 경우
            # 마지막 숫자가 k이상일때
            if heapq.heappop(scoville_heap) >= K: 
                return mix_count
            else:
                return -1
    
        min1 = heapq.heappop(scoville_heap)
        if min1 >=K:
            print(mix_count)
            return mix_count
        min2 = heapq.heappop(scoville_heap)
        
        new = min1 + min2*2
        heapq.heappush(scoville_heap, new)
        
       
        mix_count+=1