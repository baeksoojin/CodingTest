import itertools

def solution(word):
    answer = 0
    
    # 백트래킹 느낌 -> 중복제거 순열조합으로 풀이
    base = ['A', 'E', 'I', 'O', 'U']
    
    word_set = set()
    for i in range(1, 6):
        
        words = list(itertools.product(base, repeat = i))
        for w in words:
            word_set.add(''.join(w))
    
    word_list = list(word_set)
    word_list.sort()
    return word_list.index(word)+1