n = int(input())

def Recursion(n):
    if n==1:
        return n
    return n * Recursion(n-1)

if n==0:
    print("1")
else:
    print(Recursion(n))
# 12까지 주어져서 깊이가 1000을 넘기지 않아서 setrecursionlimit을 변경하지 않아도됨

