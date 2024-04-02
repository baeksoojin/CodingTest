'''
그리디? 남은 시간이 적은 쪽으로 사람을 보내면 되지 않나?
근데 남은 시간이 적은 쪽을 시간마다 체크해야함. 그러나,입국 심사를 기다리는 사람이 10의 9승. 1억 -> 다른 방법을 사용해야한다.

심사를 받는 시간의 최솟값을 탐색해야함.
시간이 정해지면, 처리할 수 있는 최대 인원수가 정해짐. 이때 n보다 최대인원수가 크거나 같다면 시간을 줄임(mid를 max로 변경)
'''


def solution(n, times):
    answer = 0
    
    # n명을 가장 빠르게 처리할 수 있는 가능한 시간
    start = min(times)
    # n명을 가장 느리게 처리할 수 있는 시간
    end = max(times) * n
    
    
    while True:
        if start> end:
            return start
        
        mid = (start+end)//2
    
        # mid시간일때, 처리가능한 최대 사람수
        max_n_at_mid = 0
        for time in times:
            max_n_at_mid += mid // time
            if max_n_at_mid > n:
                break
        # start랑 end가 동일하거나 start가 end보다 커지느 순간 stop -> 둘중 하나 출력
        # 최대가능한 숫작다 n보다 적다면 최대처리 가능한 숫자가 커져야하니, 시간을 늘려줌 -> mid를 start위치로
        if max_n_at_mid < n:
            start = mid+1
        else:
            answer = mid
            end = mid-1
    
    return answer