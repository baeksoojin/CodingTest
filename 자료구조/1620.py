# 딕셔너리를 사용해서 번호를 저장. 이름을 key로 하고 value를 index로 설정하자.

import sys
input = sys.stdin.readline
n ,m = map(int,input().split())

key_name = {} # 이름을 입력했을 때 숫자가 나오도록
key_num = {} # 숫자를 입력했을 때 이름이 나오도록

for i in range(1,n+1):
    name = input().strip()
    key_name[name] = str(i)
    key_num[str(i)] = name

for _ in range(m):
    ques = input().strip()
    # 이름으로 입력받을 때
    if ques in key_name.keys():
        print(key_name[ques])
    else:
        print(key_num[ques])