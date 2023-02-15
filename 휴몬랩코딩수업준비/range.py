'''
for문과 range

# range(num)

    for x in range(num):
        print(x)

    x에 num-1의 숫자가 들어가며 반복된다.

    <result>
    0
    1
    2
    3
    ...반복할 횟수에 해당하는 숫자 -1

# start와 end => range(start, end)

    0부터 시작하고 반복할 횟수만큼 진행되니까 반복할 횟수가 n일때 n-1까지의 숫자가 변수에 담기며 반복문이 실행됨

    사실 0은 생략된 것이고 range(num)은 range(0, num)과 같은 표현이다.

    1. 
        for i in range(0,num):
            print(i)

    2. for i in range(num):
            print(i)

    1.과 2는 "같은" for문이다. 
    => range는 범위이기에 start, end값이 존재해야하는데 "start"부터 시작해서 "end-1"가 변수에 들어가게 된다. 
    => 따라서 (end-start)번의 반복이 진행된다.


    # 예시

    for i in range(2,4):
        print(i)

    결과는?
    2
    3
    (총 2번의 for문이 실행)

# step추가 range(10,0,-2)

    for x in range(start, end, step):

    1. start : 시작정수
    2. end : end미만의 값을 발생시킴
    3. step :  발생되는 정수의 간격

    변수의 값이 10에서 시작하여 -2만큼의 step변화를 가지게 되며 for문을 도는데 0은 포함하지 않아서 2까지 출력됨

    예시
    print list(range(10,0,-2))
    
    <result>
    [10,8,6,4,2]



-------------

# range가 없을 때

for i in [1,2,3]:
    print(i)

<result>
1
2
3

리스트인 [1,2,3]안에 담긴 값이 하나씩 꺼내지면서 for문을 돌다가 더이상 꺼낼 값이 없을 때 for문의 실행을 중지한다.


'''


# 1. range(n) 연습 : 정수 n을 입력받고 1부터 n까지 출력


# 2. range(start, end)연습 : 정수 a,b를 입력받고 a+1부터 b-2의 숫자까지 출력한다. a와 b의 차이는 3이상 나게 입력.


# 3. 1부터 10까지 3의 배수만 출력하는데 if문을 사용하지 않는다. 
