'''
하노이의 탑은 재귀를 사용한다.
-> n,start, to, via인데 여기서는 to가 3에서 시작 start가 1로 시작. via가 2로 시작. (a,b,c)로 시작한다.
이때, 하노이의 탑은 N=1일때 1이고 여기서 재귀가 끝나야한다.

n=2 
1. n=1 -> (a,b)로 이동 -> 1을 가지고 3으로 옮기는 횟수와 동일 hanoi(1, a,b)을 재귀로 실행. 
2. n=2 -> (a,c)로 이동 -> 자기자신을 3으로 옮기는 횟수(move하는 방법을 진행) (1회 고정)
3. n=3 -> (b,c)로 이동 -> 1을 가지고 3으로 옮기는 횟수와 동일 hanio(1,b,c)을 재귀로 실행.
'''


def move(n,start, end, answer): # move를 통해서 어디서 어디로 이동하는지 저장하고 hanoi 재귀를 통해서 실행

    #print('{}번 원반을 {} -> {}'.format(n,start, end))
    answer.append([start,end])
    

def hanoi(n, start, end, via, answer):
    
    if n==1:
        move(1, start,end, answer)
        return
    
    hanoi(n-1, start, via, end, answer) # 3번째를 거쳐서 2번째로 가야 다음에서 3번째의 위치에 n번째 링을 3번으로 옮길 수 있음
    move(n-1, start, end, answer)
    hanoi(n-1, via, end, start, answer) # 현 위치에서 결국 3번재 링으로 와야함
    return answer
    

def solution(n):
    
    answer = []
    
    if n==1:
        return [1,3]
    elif n==2:
        return [ [1,2], [1,3], [2,3] ]
    else:
        return hanoi(n, 1,3,2,[])
         