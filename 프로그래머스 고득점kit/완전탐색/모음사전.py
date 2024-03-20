'''
1. n과 m을 사용해서 깊이우선 탐색을 진행
-> 2. 깊이우선 탐색을 진행


3월 20일 2시16분 시작 ~ 2시 48분 끝
'''


from collections import deque

alphabet = ['A', 'E', 'I', 'O', 'U']
size = 5

result = 0
answer = 0
    
def find_word_result(current, dep, word):

    
    global result
    global answer
    
    # 현재 숫자가 찾는 숫자인지 체크하고 지금ㄲ지의 counting결과를 넣기
    if current == word:
        answer = result
        return True
    
        
    if dep==5:
        return 
    
    for i in range(size):
        next_word = current + alphabet[i]
        result+=1
        flag = find_word_result(next_word, dep+1 , word)
        if flag == True:
            return
            
def solution(word):
    find_word_result('', 0, word)
    return answer


'''
백트래킹을 사용했는데 근데 python 의 중복수열을 사용하면 편리하다고 봤다.
-> 다른 사람의 풀이)
from itertools import product

1. product(배열, repeat = n) -> n을 1부터 5까지해서 전부 배열에 저장.
2. 순서가 사전순이 아닐 것임 -> 사전순으로 정렬해야함 -> sort를 사용
3. for문 돌면서 index를 1씩 증가시키고 일치할때 print
'''

# 아래와 같이 풀이한다.
from itertools import product

test = ['A','E']
all_case = []
for i in range(2):
    for j in product(test, repeat = i+1):
        all_case.append(j)

find = 'AE'
all_case.sort()
print(all_case)

result = 0

for case in all_case:
    result +=1
    if ''.join(list(case)) == find:
        print(result)
        break

print(result)