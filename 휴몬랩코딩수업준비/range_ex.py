
# 1. range(n) 연습 : 정수 n을 입력받고 1부터 n까지 출력

n = int(input())
for i in range(n):
    print(i+1)

# 2. range(start, end)연습 : 정수 a,b를 입력받고 a+1부터 b-2의 숫자까지 출력한다. a와 b의 차이는 3이상 나게 입력.
a,b = map(int, input().split())
for i in range(a+1, b-1):
    print(i)

# 3. 1부터 10까지 3의 배수만 출력하는데 if문을 사용하지 않는다. 

for i in range(3,10,3):
    print(i)