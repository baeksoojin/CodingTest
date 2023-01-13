'''
주어진 채널과 가장 차이가 적게 나도록 숫자를 구성해야함.
if) 5457일때 사용못하는 숫자가 678일때 1,2,3,4,5,9,0 사용이 가능하다는 것임.
1,2,3,4,5,9,0으로 5457이과 가장 차이가 적게나게 만들려면 5457에서 1씩 줄이거나 1씩 더하는 과정을 반복하면서 해당 숫자가 만들어 질 수 있는지를 파악하면 될 것 같음.

count = 1 -> 한번의 증가 혹은 감소) 5458, 5456 -> 사용할 수 없는 수가 두개의 경우 모두 존재함
count = 2 -> 한번의 증가 혹은 감소) 5459, 5455 -> 사용할 수 있는 수가 존재하는 경우가 1개 이상 존재함 -> 현재의 count는 2
결론은 채널을 만들기 위해서 필요한 temp채널(현재는 5459 혹은 5455)의 자릿수 + count 결과값 => 최종 6이됨

시간초과)
모든 채널이 고장났을 때를 고려하지 않아서 whlie문을 빠져나오지 못함

이후) 틀렸습니다.
10%에서 틀렸습니다가 나옴...이유는? 모르겠음.

다시 생각해보니 temp_ch에 들어가야하는 초기값이 INF값이 아닌 100에서 +와 -로만 움직이는 경우가 된다.
따라서 temp_ch에 들어가는 수를 abs(100-channel)로 했어야함.

이후) 틀렸습니다
50%에서 틀렸습니다.가 나와서 코드를 짜면서 생각하지 못한 부분이 있는 것 같으데....
따라서 복잡하게 up,down으로 나누지 말고 
처음부터 모든 수를 탐색해가면서 min값을 찾는 코드로 변경하려고 생각함.

'''

# import sys
# input = sys.stdin.readline

# CURRENT = 100
# INF = int(1e10)

# channel = int(input())
# n = int(input())

# break_ch = []
# if n!=0:
#     break_ch = list(input().split())

# count = 1


# def check(num):

#     for i in num:
#         if i in break_ch:
#             return False
#     return True

# def min_count(down, up):

#     global count
#     count = 1
#     temp_ch = abs(100-channel)
        
#     while(up<=1000000 or down>=0):
        
#         if channel == CURRENT: # 입력받은 채널이 100일때
#             return 0
#         elif check(set(str(channel))): #한번에 갈 수 있을때 -> 리모컨 버튼만으로만 갈 수있을때
#             return len(str(channel))
#         elif n==10:
#             return abs(100-channel)
#         else:

#             # down, up이 각각 만들 수 있는 채널인지 확인

#             for i in [down,up]:
#                 if check(str(i)):
#                     temp_ch = min(temp_ch,len(str(i))+count)

#             down -=1
#             up +=1
#             count +=1
            
#     return temp_ch
            
# down, up = channel-1, channel+1

# print(min_count(down, up))


'''


단순하게 0번의 채널부터 500,000의 채널까지를 순차적으로 탐색하면서 완전탐색을 진행
탐색 : 주어진 버튼으로 이동이 가능한 채널을 대상.(temp_channel)

이동 가능한 채널이 최종으로 보여져야하는 채널과 몇번의 리모컨 이동
1.(temp_channel과 channel의 차이의 절댓값이 +혹은  - 버튼을 눌러야하는 개수)
2.temp_channel을 string으로 만들고 len을 체크하면 숫자로 누르는 버튼의 개수
1+2를 하고 min값과 비교해서 최종 다 돌았을 때 제일 min 값이 담김

# '''

import sys
input = sys.stdin.readline

target = int(input())
n = int(input())

break_list = list(input().split())

def check(num):

    for i in num:
        if i in break_list:
            return False
    return True


total_count = abs(100-target)

if target==100:
    print("0")
elif n==10:
    print(abs(100-target))
else:
    for i in range(1000001):
        
        if check(str(i))==False:
            continue
            
     
        total_count = min(total_count, abs(i-target) + len(str(i)))

    print(total_count)

# 더 빠르고 간단하게 구현이 가능했음. -> 해결완료