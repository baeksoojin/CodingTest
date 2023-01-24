'''
양끝을 서로 index를 늘리면서 비교함.(홀수개라면 2로 나눈 몫만큼만 check)
'''

import sys
input = sys.stdin.readline

while(True):
    num = input().strip()
    if num =='0': break
    
    flag=True
    for i in range(len(num)//2):
        if num[i]!=num[len(num)-1-i]:
            print("no")
            flag = False
            break
    if flag==True:
        print("yes")