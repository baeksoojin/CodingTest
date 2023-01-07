#1로 만들어야하는데 이때, n은 10^6보다 작거나 같은 수
# 동적 프로그래밍을 이요해서 작은 값부터 채워나간다. 핵심은 이전(-1했을 때)와 비교해서 더 적은 counting값을 유지해얗나다는 것.

# 나누는 연산을 우선순위로 한다.
# 1을 빼고 더 큰 수로 나누는 과정이 더 연산횟수가 위의 경우보다 작아질 수 있으니 해당 값과 비교한다.

n = int(input())

result = [0]*(1000001)
result[2]=1

for i in range(3,n+1):
    result[i] = result[i-1]+1
    if i%3==0:
        result[i] = min(result[i],result[i//3]+1)
    if i%2==0:
        result[i] = min(result[i], result[i//2]+1)

print(result[n])

# baekjoon에서 cache를 n+1 size만큼 할당했을 때 런타임에러 ->이유를 모르겠음....
# 우선 최대로 입력받을 수 있는 수가 index최대값이 되도록 설정 -> 해결완료는 했지만 위의 케이스가 틀린이유는..?


