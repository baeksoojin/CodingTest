'''
공격을 받을 때마다 10씩 감소 -> 100에서 시작하는 프로그램 만들기
'''

class User:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def getHp(self):
        return self.hp

    def increaseHp(self):
        self.hp = self.hp + 10
    
    def decreaseHp(self):
        self.hp = self.hp - 50

    def getHp(self):
        return self.hp
    
users = list(input("대결상대를 2명 공백으로 분리하여 입력하세요").split())
user1 = User(users[0],100)
user2 = User(users[1], 100)


# 이긴사람을 입력
print()
while(1):
    if user1.hp <= 0 or user2.hp <= 0:
        if user1.hp>0:
            winner = user1
        else:
            winner = user2
        print("최종 결과 ----->이긴 사람 : ", winner)
        break
    else:
        winner = input("이긴사람 입력 : ")
        if not winner in users:
            print("잘못입력하였습니다.")
            continue
        if user1.name == winner:
            user1.increaseHp()
            user2.decreaseHp()
        else:
            user2.increaseHp()
            user1.decreaseHp()
        
        print("user1의 hp : ", user1.hp , "user2의 hp : ", user2.hp)





