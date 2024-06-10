n = int(input())
balloon = list(map(int, input().split()))

# 화살의 여부
flag_by_hei = [0] * 1000001

for b in balloon:
    
    if flag_by_hei[b]: # 화살이 있다면 -1
        flag_by_hei[b] -=1
    flag_by_hei[b-1] +=1 # 화살 추가 및 한칸 내리기

print(sum(flag_by_hei))