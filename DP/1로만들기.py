# 배열을 만들고 1부터 체크해서 연산량을 저장하면서 이후에 써먹기

count = [0]*30001

n = int(input())

for i in range(2,n+1):

    count[i] = count[i-1] + 1 # 각 경우와 비교해서 적은 결과가 나오는 것으로 채택

    if i==2:
        count[i] = 1
    if i%5==0:
        count[i] = min(count[i],count[i//5]+1)
    if i%3==0:
        count[i] = min(count[i],count[i//3]+1)
    if i%2==0:
        count[i] = min(count[i],count[i//2]+1)


print(count[n])

# baekjoon 문제와 동일함 -> 체점을 못 해봤었는데 위의 코드는 틀린 코드였었음.
# elif가 아닌 if로 바꿔줘야하는게 아무리 제일 큰 값으로 나눈 후에 어떤 연산이 진행되는지 모르기때문에 그 결과가 최소연산 횟수보다 커질 수 있다는 점을 고려해야함.

