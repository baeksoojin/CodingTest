def solution(participant, completion):
    answer = ''
    
    dict = {}
    for i in range(len(participant)):
        if participant[i] in dict.keys():
            
            dict[participant[i]] +=1
        else:
            dict[participant[i]] =1
            
    for i in completion:
        if i in dict.keys():
            dict[i] -=1
            
    
    for name,cnt in dict.items():
        if cnt!=0:
            print(name)
            answer = name
            
    return answer