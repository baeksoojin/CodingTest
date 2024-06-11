'''
6월 11일 9시 4분 시작

9시 24분까지 문제이해

1. n진수로 변경
2. 소수 찾기 -> 0으로 split

------

def change_k_number(): -> k진수로 변경

k로 나눈 나머지를 계속 저장. 몫이 k보다 작을 때까지 반복

-------

1. split by 0
2. number 중에서 0을 포함하지 않는 것만 filter

---
조건에 부합할 때 소수인지 체크

----

문제 풀이 시작 9시 10분

'''

import math

def change_k_number(k, num):
    
    result = []
    q = num # 몫
    while q >= k:
        
        r = q % k # 나머지
        result.append(r)
        q = q // k
    
    result.append(q)
    return result[::-1]
        
def is_prime(n):
    
    n = int(n)
    
    if n==1:
        return False
    
    for num in range(2, int(math.sqrt(n))+1):
        
        if n % num == 0:
            return False
    
    return True
        

def solution(n, k):
    
    # 1. n진수로 변경
    k_number = change_k_number(k, n)
    k_number = list(map(str, k_number))
    k_number = ''.join(k_number)
    
    # 2. 만족하는 소수찾기
    
    splited = k_number.split("0")
    print(splited)
    
    count=0
    
    for s in splited:
        if len(s)>0 and not '0' in s and is_prime(s):
            count+=1
    
    return count