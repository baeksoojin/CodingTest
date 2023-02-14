# 5904는 재귀를 통해서 나눠서 처리해야하는 분할정복 문제

# n = int(input())

# moo_temp = "moo"
# k = 1

# while(True):
    
#     if len(moo_temp)>=n:
#         print(moo_temp[n-1])
#         break
#     else:
#         mid_temp = ["o"]*(k+2)
#         mid_temp = ''.join(mid_temp)
        
#         m_count = moo_temp.count("m")
#         moo_temp =moo_temp + "m"+ mid_temp+ moo_temp
#         # print("k",k,"moo",moo_temp)
#         k+=1


'''
3가지로 나눠보면

해당 길이를 넘으면 
길이만 가지고 일단 판단하고 영역이 정해졌으면 그때 판단
1. 앞의 영역에 해당될때 -> 그 영역에서도 3가지 중 어딘지 판단
2. 중간 영역일때 -> 그 영역에서 첫번째라면 "m", 다른 영역이라면 "o"
3. 뒤의 영역일때 -> 다시 처음부터 실행하게 하는데 길이를 줄여서 넘김.(길이를 줄일 수 있는게 사이즈에 규칙이있기 때문임)
'''

moo_temp = "moo"

def recursive(n,k,before_len):

    len_temp = 2*before_len + (k+3)
    # print(n,k,before_len)
    if n<=3:
        print(moo_temp[n-1])
        return
    
    if len_temp >= n:
        # 앞에는 어차피 없었음
        # 중간
        if before_len<n<=before_len+k+3:
            if n-before_len==1:
                print("m")
                return
            else:
                print("o")
                return
        else:#뒤일때
            recursive(n-(before_len+k+3),1,3)
    else:
        recursive(n,k+1,len_temp)
    

# n = int(input())
recursive(n,1,3)
    


    
