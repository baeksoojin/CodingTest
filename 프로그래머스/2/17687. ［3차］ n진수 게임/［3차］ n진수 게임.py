def to_n_number(num, n):
    
    answer = []
    

    if num==0:
        return [0]

    alp = ['A','B','C','D','E','F']
    
    while num!=0:
        
        r = num%n if num%n <=9 else alp[(num%n)-10]
        answer.append(r)
        num = num//n
    
    return answer[::-1]
    
    

def solution(n, t, m, p):
    answer = ''
    
    
    # 게임에 참가하는 인원 m과 튜브의 순서 p가 주어짐 ->  m으로 나눴을 때 나머지가 p인 것들을 출력
    
    # t개를 출력할 때까지 진법 변환을 하고 t개 출력하고 break
    
    current_t = 0
    current_num = 0
    count = 0
    flag = False

    while True:

        if current_t >= t:
            break
            
        n_num_list = to_n_number(current_num, n)
        
        for i in range(len(n_num_list)):
            if (count % m) ==p-1:# m으로 나눴을 때 현재 숫자가 p번째 순서인 경우
                answer+=str(n_num_list[i])
                current_t +=1
                if current_t == t:
                    flag = True
                    break
            
            count+=1
        current_num+=1

        if flag:
            break

            
            
    return answer