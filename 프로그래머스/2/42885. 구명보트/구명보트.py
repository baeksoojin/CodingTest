'''
돼지랑 가장 몸무게가 적게 나가는사람이랑 비교해서 못 타면 돼지는 혼자 타고 나가야함.
만약 제일 몸무게 많이 나가는 사람과 적게 나가는 사람을 합쳤을 때 구명보드에 탈 수 있다면 타면됨. 
'''

def solution(people, limit):
    answer = 0
    
    # pointer가 같아지는 순간은 1명 남은거니 +1 , 포인터가 교차된다면 break
    
    start_p = 0
    end_p = len(people) - 1
    
    people.sort(reverse = True)
    
    while True:
        
        if start_p == end_p:
            answer+=1
            return answer
        if start_p > end_p:
            return answer
        
        if people[start_p] + people[end_p] <= limit:
            start_p +=1
            end_p -=1

        else:
            start_p +=1

        answer+=1
    return answer
