'''
permutation을 사용 -> permutation은 안 구해도 되는 범위까지 구하게 된다.(시간초과)
백트킹으로 풀려고했는데 -> 이거는 재귀를 사용하며 가지치기를 해서 n^2이 시간복잡도 (시간초과) -> 10까지만 해도 괜찮았을텐데 지금 20임
팩토리얼을 사용해서 이전수와 다음수를 알 수 있다. 몫과 나머지를 사용하는 방법
'''

def factorial(n):
    answer = 1
    for i in range(n):
        answer *= (i+1)
    return answer
    

def solution(n, k):
    n_list = []
    
    for i in range(1,n+1):
        n_list.append(i)
        
    # n=1개일때를 처리
    if n==1:
        return [1]

    # 초기화
    q = r = 0
    answer = []

    while n!=0:
        fac = factorial(n-1)
        q = k//fac
        k = k%fac # k를 변경시켜준다.
        
        if k==0:
            answer.append(n_list.pop(q-1)) #k=0(2개남았을 때, 1개남았을 때) 일때는 반대로 출력하도록 한다.
        else:
            answer.append(n_list.pop(q))
        
        n-=1
    
    return answer
