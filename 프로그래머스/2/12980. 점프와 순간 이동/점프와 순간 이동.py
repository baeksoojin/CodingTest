'''
12시 14분 시작
수학문제
규칙 -> 나머지와 몫을 사용해서 해결 가능



while not(n == 1):
    if (n % 2) == 1:
        answer+=1
    n = n//2
    
answer+=1

    

'''


def solution(n):
    answer = 0
    
    while not(n == 1):
        if (n % 2) == 1:
            answer+=1
        n = n//2
    
    answer +=1

    return answer