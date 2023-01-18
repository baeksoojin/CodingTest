'''
비밀번호 찾기
dictionary를 사용
'''

import sys
input = sys.stdin.readline

n,m = map(int, input().split())

account = dict()
for i in range(n):
    site, pw = input().split()
    account[site.strip()] = pw.strip()

for j in range(m):
    site = input().strip()
    print("result======>",account[site])
    