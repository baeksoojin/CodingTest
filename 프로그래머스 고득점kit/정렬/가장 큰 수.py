
from itertools import permutations
from itertools import permutations

def solution(numbers):
    answer = []
    
    numbers_str = list(map(str, numbers))
                      
    # 가장 앞의 수를 기준으로 정렬 -> 문자열 곱하기! -> 같은 문제열을 n번 반복
    numbers_str.sort(key = lambda x : (x*3), reverse=True)
    return str(int(''.join(numbers_str)))

    ''' 시간초과 '''
    # head_number = numbers_str[0][0] # 가장 앞에 있는 수의 첫번째 수를 저장
    # head_number_list = []
    # head_number_list.append(numbers_str[0])
    # for i in range(1,len(numbers_str)):
    #     if numbers_str[i][0] != head_number: # 다를 경우, head_number들중 만들 수 있는 가장 큰 수를 저장
    #         # head_number_list의 조합으로 만들 수 있는 가장 큰 수 찾고 answer에 추가
    #         permutation_result = list(permutations(head_number_list,len(head_number_list)))
    #         max_temp = '0'
    #         for p in permutation_result:
    #             current_value = ''.join(p)
    #             if max_temp < current_value:
    #                 max_temp = current_value
    #         #print(max_temp)
    #         answer.append(max_temp)
    #         #head_number를 다음 값으로 변경하기
    #         head_number = numbers_str[i][0]
    #         #print("head_number->", head_number, "index -> " ,i)
    #          # head_number_list 초기화
    #         head_number_list = []
    #         head_number_list.append(numbers_str[i])
                
    #     else: #head_number가 같으니 head_number_list에 저장
    #         head_number_list.append(numbers_str[i])

    # permutation_result = list(permutations(head_number_list,len(head_number_list)))
    # max_temp = '0'
    # for p in permutation_result:
    #     current_value = ''.join(p)
    #     if max_temp < current_value:
    #         max_temp = current_value
    # answer.append(max_temp)