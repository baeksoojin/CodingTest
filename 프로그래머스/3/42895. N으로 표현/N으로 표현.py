'''
dp를 뭘로 사용하냐에 따라서 달라짐.
여기서는 result를 사용해서 최적해를 찾는다.

1. result를 만들 수 있는 경우의 수-> 다음 경우의 수에 영향을 줌
2. number를 만들 수 있는 경우의 수 -> number가 정해질때를 위한 규칙이 없으니 탈락
3. N이 변경될때의 경우의 수 -> 규칙 없음.

3개중에서 1번째가 후보가 된다. 벽지 타일 문제와 비슷하다.

최솟값이 8보다 크면 -1을 return 하면 되니까 8까지만 돌면됨.
'''

def solution(N, number):
    
    
    answer = 0
    
    
    # 각 횟수당 만들 수 있는 숫자를 저장하고 이를 활용해야함.
    
    numbers = [[] for _ in range(9)]
    
    # 이중 포문을 돌면서 0~i의 경우일때 각각 i~0일때와 함께 조합하고 그 숫자를 저장.
    # 계산을 안 해도 나오는 경우 -> N을 반복사용하는 경우, -> 가장 처음에 넣고 시작.
    
    
    for i in range(1, 9):
        
        # N만 사용해서 나올 수 있는 경우의 수 넣기
        
        combs = set()
        combs.add(int(str(N)*i))
        
        # 만들 수 있는 경우의 수를 돌리기
        for j in range(1,i):
            for comb1 in numbers[j]:
                for comb2 in numbers[i-j]:
                    # 더하기
                    combs.add(comb1+comb2)
                    # 빼기
                    if comb1-comb2 >=1:
                        combs.add(comb1-comb2)
                    # 나누기
                    if comb1//comb2:
                        combs.add(comb1//comb2)
                    # 곱하기
                    combs.add(comb1 *comb2)
        
        
        # 최종 combination 결과들을 모두 저장
        
        # 해당 조합의 결과로 찾는 숫자가 나왔는지 체크
        if number in combs:
            print(number)
            return i
            break
        numbers[i] = list(combs)
    
    return -1