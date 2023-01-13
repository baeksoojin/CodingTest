'''
1시 51분 시작

주어진 채널과 가장 차이가 적게 나도록 숫자를 구성해야함.
if) 5457일때 사용못하는 숫자가 678일때 1,2,3,4,5,9,0 사용이 가능하다는 것임.
1,2,3,4,5,9,0으로 5457이과 가장 차이가 적게나게 만들려면 5457에서 1씩 줄이거나 1씩 더하는 과정을 반복하면서 해당 숫자가 만들어 질 수 있는지를 파악하면 될 것 같음.

count = 1 -> 한번의 증가 혹은 감소) 5458, 5456 -> 사용할 수 없는 수가 두개의 경우 모두 존재함
count = 2 -> 한번의 증가 혹은 감소) 5459, 5455 -> 사용할 수 있는 수가 존재하는 경우가 1개 이상 존재함 -> 현재의 count는 2
결론은 채널을 만들기 위해서 필요한 temp채널(현재는 5459 혹은 5455)의 자릿수 + count 결과값 => 최종 6이됨

시간초과)
모든 채널이 고장났을 때를 고려하지 않아서 whlie문을 빠져나오지 못함

이후) 틀렸습니다.
10%에서 틀렸습니다가 나옴...??


'''

import sys
input = sys.stdin.readline

CURRENT = 100
INF = int(1e10)

channel = int(input())
n = int(input())

break_ch = []
if n!=0:
    break_ch = list(input().split())

count = 1

def check(check_set):

    for i in break_ch:
        if i in check_set:
            return False
    return True

def min_count(down, up):

    global count
    count = 1
        
    while(1):
        
        if channel == CURRENT: # 입력받은 채널이 100일때
            return 0
        elif check(set(str(channel))): #한번에 갈 수 있을때 -> 리모컨 버튼만으로만 갈 수있을때
            return len(str(channel))
        elif len(break_ch)==10:
            return abs(100-channel)
        else:

            temp_ch = INF

            # down, up이 각각 만들 수 있는 채널인지 확인

            for i in [down,up]:
                if check(set(str(i))):
                    temp_ch = min(temp_ch,len(str(i))+count)

            if temp_ch!=INF:
                return temp_ch
            else:
                down -=1
                up +=1
                count +=1
            
            
down, up = channel-1, channel+1

print(min_count(down, up))
