#수평으로 두칸이동후에 수직으로 한칸 이동
# 수직으로 두칸 이동후에 수평으로 한칸 이동
# 8*8의 평면으로 고정
# 시작지점을 1,1로 설정

from re import I


goal = input()
i = int(goal[1])
j = int(ord(goal[0])) - int(ord('a')) + 1


#갈 수 있는 경우
steps = [(2,1),(2,-1),(-2,1),(-2,1),(1,2),(1,-2),(-1,2),(-1,-2)]
count = 0

for s in range(8):
    next_i = i + steps[s][0]
    next_j = j + steps[s][1]

    if next_i <=8 and next_i >=1 and next_j <=8 and next_j>=1:
        count += 1


print(count)