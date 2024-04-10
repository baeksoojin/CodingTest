'''
7시 20분 시작.
7시 25분까지 문제 이해.
7시 30분까지 예제 이해.
7시 40분까지 알고리즘 정리.

n-> size
n_list -> n개 + n-1개
for i in range(n):
    temp = 0
    for j in range(n):
        set.add(temp + n_list[i+j])
'''

def solution(elements):
    answer = 0
    n = len(elements)
    element_list = elements + elements[:-1]
    #print(element_list)
    answers = set()
    
    for i in range(n):
        temp = 0
        for j in range(n):
            answers.add(temp + element_list[i+j])
            temp = temp + element_list[i+j]
        
    #print(answers)
    return len(answers)