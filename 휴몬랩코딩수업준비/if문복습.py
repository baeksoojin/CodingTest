'''
책 149쪽 05번 문제 풀이 => 10시10분까지 풀기.

'''

import random

x = random.randint(1,100)
y = random.randint(1,100)

op = random.choice(["+","-","*","/","%"])

user_answer = int(input("{0} {1} {2} = ".format(x,op,y)))

if op =="+":
    answer = x+y
elif op=="-":
    answer = x-y
elif op=="*":
    answer = x*y
elif op=="/":
    answer = x/y
else:
    answer = x%y

if answer==user_answer:
    print("정답입니다.")
else:
    print("틀렸습니다. 정답은 {0} 입니다.".format(answer))