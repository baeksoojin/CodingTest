# 팰린드롬
n = int(input())
checklist =[]

for _ in range(n):
    checklist.append(input())

def recursion(s, l, r):
    if l>=r:
        return 1, l+1
    elif s[l] != s[r]:
        return 0, l+1
    else:
        return recursion(s, l+1, r-1)


for i in range(n):
    # 재귀함수 실행
    result, count = recursion(checklist[i], 0, len(checklist[i])-1)
    print(result, count)
