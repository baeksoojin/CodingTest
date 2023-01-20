'''
2시 40분 시작. -> 50분 끝.

규칙을 보니 11122까지는 그냥 저장하고 그 다음부터 (index-5 + 직전값)의 결과가 나오는 것을 확인할 수 있었다.

'''

t = int(input())

size = [0]*101
size[1] = 1
size[2] = 1
size[3] = 1
size[4] = 2
size[5] = 2
for i in range(6,101):
    size[i] = size[i-5] + size[i-1]

for i in range(t):
    n = int(input())
    print(size[n])