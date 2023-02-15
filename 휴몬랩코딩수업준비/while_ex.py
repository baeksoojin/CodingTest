#1
i = 2

while(i<11):
    print(i)
    i+=2


#2
for i in range(1,21):
    if i%3==0:
        continue
    print(i)

#3


year, total_money, plus_money, rate = 0,0,2000, 1.06

goal = 100000

while True:
    year+=1
    total_money = (total_money+plus_money)*rate
    if total_money >= goal:
        break

print("{0} 뒤에 10억을 넘기고 {1}원이 됩니다".format(year,int(total_money)))

