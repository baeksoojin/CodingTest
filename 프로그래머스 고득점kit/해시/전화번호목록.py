def solution(phone_book):
    answer = True
    
#     for i in range(len(phone_book)):
#         check_num = phone_book[i]
#         check_size = len(check_num)
#         for j in range(len(phone_book)):

#             if check_num == phone_book[j][:check_size] and i!=j:
#                 print(check_num)
#                 answer = False => 시간초과 (O(n^2)이니까 시간초과)

    dic = {}

    for i in range(len(phone_book)):
        
        phone_num = phone_book[i]
        for j in range(len(phone_num)-1):
            dic[phone_num[:j+1]]=1
            
    for p in phone_book:
        if p in dic.keys():
            return False

    return answer