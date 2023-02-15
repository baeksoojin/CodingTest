'''
# while문 기본
    while condition:
        실행문장1
        ...

    condition이 True일때 실행문장들을 실행하며 False일때까지 "무제한"반복

    # 예제코드
    x=0
    my_list=["10","20","30","40","50,"60"]
    while x<4:
        print(my_list[x])
        x+=1
    print("loop end")

    <결과는?>


# 중지조건

1. break를 만나면 바로 위에 있는 반복문을 바로 빠져나온다.

    while True:
        sum += cnt
        cnt+=1
        if cnt>10:
            break
    print(sum)

    result?


2. continue를 통해서 바로 위에 있는 반복문의 시작으로 이동한다.

    for i in range(1,6):
        if n==4:
            continue
        print(n,end=" ")
    print("finish")

    result => 1,2,3,5





'''

# while문을 사용해서 1과 10사이의 수 중에서 2의 배수를 출력(if문을 사용하지 말것)


# 3의 배수인 경우, 출력하지 않고 다음 숫자로 넘어가야하는 369게임이 있을 때, 1부터 20까지 369게임을 적용해서 숫자를 출력해보자.


# 연이율이 6%이고 매년 2000만원을 저축할때, 몇년을 저축해야 10억을 마련할 수 있을지 while문과 break를 통해서 작성. 이때 출력시 돈은 int형으로한다.

year, total_money, plus_money, rate = 0,0,2000, 1.06

goal = 100000

while True:
    year+=1
    total_money = (total_money+plus_money)*rate
    if total_money >= goal:
        break

print("{0} 뒤에 10억을 넘기고 {1}원이 됩니다".format(year,int(total_money)))

