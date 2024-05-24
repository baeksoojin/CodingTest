'''
한자리 숫자가 적힌 종이 조각
1. 완전탐색을 진행.
2. 소수판별
'''
import itertools
import math

def is_prime(number):
    
    if number == 0 or number==1:
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True
    
def solution(numbers):
    answer = 0
    answers = set()
    
    number_list = []
    for i in range(len(numbers)):
        number_list.append(numbers[i])
    #print(number_list)
    
    # combination
    for i in range(len(numbers)):
        comb_list = list(itertools.permutations(number_list, i+1))
        #print(comb_list)
        
        for comb in comb_list:
            num = int(''.join(comb))
            if is_prime(num): # 소수라면 set에 저장
                answers.add(num)
                
    #print(answers)
    return len(answers)