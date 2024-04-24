from itertools import product


def solution(word):
    answer = 0
    
    # 모든 가능한 조합을 저장
    answers = set()
    words = [ 'A', 'E', 'I', 'O', 'U']
    
    for i in range(1,6):
        product_list = list(product(words, repeat = i))
        for p in product_list:
            word_temp = ''.join(p)
            answers.add(word_temp)
            
    answer_list = list(answers)
    answer_list.sort()
    return answer_list.index(word)+1