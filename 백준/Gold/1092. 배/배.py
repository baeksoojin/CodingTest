
n = int(input())
c_list = list(map(int, input().split())) # 크레인
m = int(input())
b_list = list(map(int, input().split())) # 박스의 무게

if max(b_list) > max(c_list):
    # -1처리
    print(-1)
else:
    # 오름차순 정렬
    c_list.sort(reverse= True)
    b_list.sort(reverse = True)
    time = 0
    index= 0 
    while b_list:
        
        time+=1

        # 크래인 무게보다 더 적은 것 중에서 가장 큰 것을 제거
        for c_w in c_list:

            if b_list and c_w < b_list[-1]:
                break
            for b_w in b_list:
                if b_w <= c_w:
                    b_list.remove(b_w)
                    break
    print(time)

