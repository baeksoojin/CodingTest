'''
원가와 할인율을 입력받고 금액을 출력하는 계산기 class 만들기
'''

class Calc:

    def __init__(self, money, rate):
        self.money = money
        self.rate = rate

    def discount(self):
        self.money = self.money - self.money*(self.rate/100)

    def getMoney(self):
        return int(self.money)

money, rate = map(int,input("원가와 할인율을 입력(공백단위)").split())
calc1 = Calc(money,rate)
calc1.discount()
print(calc1.getMoney())

    