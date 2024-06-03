'''
튜플의 원소들 중에서 길이가 짧은 것부터 탐색
탐색하며 원소를 하나씩 뽑아내고, 이전 원소가 아닌 원소가 다음 원소가 됨.
이전 원소를 저장해놔야함. 
'''

def solution(s):
    answer = []
    
    s_list = []
    split_temp = s.split("{")
    for temp in split_temp:
        if temp.split('}')[0] !="":
            s_list.append(list(map(int,temp.split('}')[0].split(","))))
    

    s_list.sort(key = lambda x : len(x))
    # print(s_list)
    
    s_set = set()
    
    for value in s_list:
        v = list(set(value) - s_set)[0]
        answer.append(v)
        s_set.add(v)
    
#     print(answer)
        
    
    
    return answer