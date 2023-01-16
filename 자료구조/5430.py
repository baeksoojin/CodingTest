'''
목표) 30분 (풀이 완료. 24분)

'd'직전에 나온 reverse'r'가 홀수번 일어나면 -> 뒤집힌 것으로 판단하고 d를 만난다면 뒤에서 숫자를 하나 제거함
    만약 짝수번 나온다면 -> 앞에서 하나를 제거함

답은 나오지만 왠지 시간초과 예상....!

+) 중간에 join 연산자 쓰고 싶은데 기억이 안 나서 검색,,!

join : 구분자.join(리스트)

'''

# t = int(input())

# for i in range(t):
#     p = input().strip()
#     n = int(input())
#     if n==0:
#         temp = input()
#         if 'D' in p:
#             print("error")
#             continue
#         else:
#             print("[]")
#             continue
#     else:
#         case = list(input().strip()[1:-1].split(","))
        
#         rcount = 0
#         is_error = False
#         #p 가지고 조작.
#         for j in p:
#             if j in 'D':
#                 if len(case)==0:
#                     is_error = True
#                 else:
#                     if rcount%2==0:#짝수인경우는 그대로 -> 뭔가 시간복잡도상으로 heap을 사용해야할 것 같긴함..
#                         case = case[1:]
#                     else:
#                         case.pop()
#             else:
#                 rcount+=1
#         if is_error==True:
#             print("error")
#         else:
#             if rcount%2==0:
#                 print("["+",".join(case)+"]")
#             else:
#                 case.reverse()
#                 print("["+",".join(case)+"]")


'''
역시나 시간초과 -> 시간제한은 단 1초 -> 시간복잡도 O(N)기준 10^7으로 풀 수 있음.
=> for문만 계산했을 때 10^7을 채우니 if문과 다른 연산까지 합치면 당연히 1초를 넘김...(심지어 reverse연산까지 하니까,,,,
=> reverse, index slicing -> 둘다 O(N)임

힙을 사용해보자!
index를 힙에 숫자와 함께 넣고 해당 index를 방문했는지 처리하는 배열을 만들어 False일때는 해당 숫자가 배열에 없다는 것으로 상대방 heapq에서 빼줘야함.

목표) 30분
시작 : 9시 25분 -> 10시 11분

'''


# import sys
# import heapq
# input = sys.stdin.readline

# t = int(input())
# for _ in range(t):

#     p = input().strip()
#     n = int(input())

#     max =[]
#     min=[]
#     visited =[False]*(n)
#     if n==0:
#         temp = input()
#         if 'D' in p:
#             print("error")
#         else:
#             print("[]")
#         continue


#     case = list(map(int,(input().strip())[1:-1].split(",")))
#     for index in range(n):
#         heapq.heappush(min,(index,case[index])) # index를 기준으로 정렬되어야함.(기본은 최소힙)
#         heapq.heappush(max,(-index,case[index])) # 최대힙 만들기
#         visited[index] = True # list에 존재함을 의미함.

#     #visited를 체크하면서 Flase인데 최소 혹은 최대로 뽑힌다면 그 값을 pop해주는 과정을 처음에 거쳐야함
#     rcount = 0
#     dcount=0
#     error = False
#     case_len = len(case)
#     for j in p:
#         if j == 'D':
#             dcount+=1
#             if len(case)<dcount:
#                 error = True
#                 break
#             else:
#                 if rcount%2==0:#짝수인경우는 앞에서 뽑아줌
#                     while min and not visited[min[0][0]]:
#                         heapq.heappop(min)
#                     #최소 index를 가지는 값을 뽑아줌
#                     visited[min[0][0]] = False
#                     heapq.heappop(min)
#                 else: # 홀수인경우는 Reverse가 일어나야해서 뒤에서 뽑아줌
#                     while max and not visited[-max[0][0]]:
#                         heapq.heappop(max)
#                     #최소 index를 가지는 값을 뽑아줌
#                     visited[-max[0][0]] = False
#                     heapq.heappop(max)
#         else:
#             rcount+=1

#     if error==True:
#         print("error")
#         continue

#     while min and not visited[min[0][0]]:
#         heapq.heappop(min)
#     while max and not visited[-max[0][0]]:
#         heapq.heappop(max)

#     if rcount%2==1: #큰 index부터뽑기
#         print("[", end='')
#         while(max):
#                 if len(max)==1 and visited[-max[0][0]]!=False:
#                     print(heapq.heappop(max)[1], end='')
#                 elif visited[-max[0][0]]!=False:
#                     print(heapq.heappop(max)[1],end="")
#                     print(",",end='')
#         print("]", end='')
#     else:
#         print("[", end='')
#         while(min):
#                 if len(min)==1 and visited[min[0][0]]!=False:
#                     print(heapq.heappop(min)[1],end='')
#                 elif visited[min[0][0]]!=False:
#                     print(heapq.heappop(min)[1],end='')
#                     print(",",end='')
#         print("]", end='')
#         print()
        
        



'''
생각해보니...왜 heapq를 사용했나..?
list가 아니라 그냥 deque를 사용하면 끝났을 것임!

첫번째를 list -> deque로 바꾼 후 시간초과 문제 해결

2분.

'''

from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().strip()
    n = int(input())
    if n==0:
        temp = input()
        if 'D' in p:
            print("error")
            continue
        else:
            print("[]")
            continue
    else:
        case = deque(input().strip()[1:-1].split(","))
        
        rcount = 0
        is_error = False
        #p 가지고 조작.
        for j in p:
            if j == 'D':
                if len(case)==0:
                    is_error = True
                    break
                else:
                    if rcount%2==0:#짝수인경우는 그대로 -> 뭔가 시간복잡도상으로 heap을 사용해야할 것 같긴함..
                        case.popleft()
                    else:
                        case.pop()
            else:
                rcount+=1
        if is_error==True:
            print("error")
        else:
            if rcount%2==0:
                print("["+",".join(case)+"]")
            else:
                case.reverse()
                print("["+",".join(case)+"]")
