'''
12시 35분 시작
몫을 이용 -> 수학?
12시 42분 풀이완료
'''


def solution(n,a,b):
    answer = 0

    a = a-1
    b = b-1 # 몫계산을 원활히 하기 위해 -1
    
    while True:
        
        a = a//2
        b = b//2
        answer+=1

        if a==b:
            return answer 
