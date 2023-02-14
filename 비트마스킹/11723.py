## 비트마스킹
# 20까지 들어옴
import sys

m = int(sys.stdin.readline())

bit = 0
for i in range(m):
    temp = sys.stdin.readline().rstrip().split()

    if temp[0] == "all":
        bit = (1 << 20) - 1
    elif temp[0] == "empty":
        bit = 0
    else:
        op = temp[0]
        num = int(temp[1]) - 1

        if op == "add":
            bit |= (1 << num)
        elif op == "remove":
            bit &= ~(1 << num)
        elif op == "check":
            if bit & (1 << num) == 0:
                print(0)
            else:
                print(1)

        elif op == "toggle":
            bit = bit ^ (1 << num)