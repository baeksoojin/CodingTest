'''
수를 기준으로 정렬 -> 가장 앞의 수를 기준으로 우선적으로 정렬되어야함

'''

def solution(numbers):
    
    numbers_str = list(map(str, numbers))
                      
    # 가장 앞의 수를 기준으로 정렬 -> 문자열 곱하기! -> 같은 문제열을 n번 반복
    numbers_str.sort(key = lambda x : (x*3), reverse=True)
    return str(int(''.join(numbers_str)))