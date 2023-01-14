'''

7시 10분 시작 7시 27분 완료.

-를 찾는다면 그 다음 -전까지의 숫자를 모두 더해서 minus_sum에 합을 해줌.
ex)
10 -1 +2 +3 -3 일 경우 -> 10 -(1+2+3) -3 => result

'''

text = input().split("-")

# print(text)
for i in range(0,len(text)):
    if "+" in text[i]:
        t = text[i].split("+")
        t = list(map(lambda x : int(x), t))
        t_sum = sum(t)
        text[i] = t_sum
    else:
        text[i] = int(text[i])
    
print(text[0]-sum(text[1:]))