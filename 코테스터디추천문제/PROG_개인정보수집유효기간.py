def check(today,terms_dic, p_start, p_type):
    
    flag = True
    # 시작한달 + 가능한 달의 수 :  => 오늘날짜와 같거나 넘어간 경우 => 결과에 담아야함
    mon = int(p_start[5:7]) + terms_dic[p_type]
    diff_year = 0
    next_month = ""
    if 0<mon%12<=9:
        next_month = "0" + str(mon%12)
        diff_year = mon//12
    elif mon%12==0:
        print("12 check")
        diff_year = mon//12 -1
        next_month = "12"
    else:
        diff_year = mon//12
        next_month = str(mon%12)
    limit = str(int(p_start[0:4]) + diff_year) + next_month + p_start[8:10]
    
    if limit <= (today[0:4])+ (today[5:7]) + (today[8:10]):
        print("limit",limit, "today",(today[0:4])+(today[5:7])+(today[8:10]),"false")
        flag = False
    
    return flag

def solution(today, terms, privacies):
    answer = []
    
    terms_dic = {}
    for term in terms:
        term_temp = term.split(" ")
        terms_dic[term_temp[0]] = int(term_temp[1])
    

    for privacy_index in range(len(privacies)):
        privacy_list = privacies[privacy_index].split(" ")
        if check(today,terms_dic,privacy_list[0], privacy_list[1]) == False:
            answer.append(privacy_index+1)
        
    
    return answer