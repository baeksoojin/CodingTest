
str1 = input()
str2 = input()

char_value_hash = dict()

# 1. hash생성
char_value_hash["I"] = 1
char_value_hash["V"] = 5
char_value_hash["X"] = 10
char_value_hash["L"] = 50
char_value_hash["C"] = 100
char_value_hash["D"] = 500
char_value_hash["M"] = 1000

special_char = ["IV", "IX", "XL", "XC", "CD", "CM"]
special_value = [4,9,40,90,400,900]


# 아라비아 -> 숫자
def to_roma(ara):

    result=0
    # 아라비아에서 3번 조건을 먼저 체크
    for i, str in enumerate(special_char):
        if str in ara:
            split_ara = ara.split(str)
            result += special_value[i]
            ara = ''.join(split_ara)


    # 각각 돌면서 hash 의 value를 증가
    for i in range(len(ara)):
        result += char_value_hash[ara[i]]

    return result

# 아라비아 -> 숫자 / test -> 완

roma = int(to_roma(str1)) + int(to_roma(str2))
print(roma)


char_list = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
value = [1000, 900,500,400,100,90,50,40,10,9,5,4,1]
limit = [3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3]

def to_ara(num):

    global value

    # num에서 큰 것부터 처리
    result = ""

    for i, v in enumerate(value):

        count = num // v 

        if count==0: continue
        if limit[i] < count:
            count = limit[i]

        num %= v

        if v in special_char: # 쌍으로 안 되는게 있음. -> 그거 조건 체크
            if i==1:
                limit[3] = 0
            elif i== 5:
                limit[7] = 0
            else:
                limit[11] = 0
        
        result += char_list[i]*count


    return result

print(to_ara(roma))


