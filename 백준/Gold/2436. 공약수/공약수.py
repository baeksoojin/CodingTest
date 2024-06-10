import math

gre, low = map(int, input().split())

multi = gre * low

numbers = []
# 1. find tuple by using multi -> sqrt 시초방지
for num in range(2, int(math.sqrt(multi))+1):
    # 약수일때
    if multi % num==0:
        another = multi // num
        numbers.append([num, another])

# 2. 최대공약수를 써서 answers에 저장
answers = []
for i in range(len(numbers)):
    num1 = numbers[i][0]
    num2 = numbers[i][1]

    if math.gcd(num1, num2) == gre:
        answers.append([num1, num2, abs(num2-num1)])

answers.sort(key = lambda x: x[2])
print(answers[0][0], answers[0][1])


