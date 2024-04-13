'''
2진수 변환과정
'''


def solution(s):
    zero_count = 0
    convert_count = 0
    
    while True:
        
        if int(s) == 1 and len(s) ==1:
            break
        
        # 이진변환 이전 0 제거
        one_count = s.count('1')
        zero_count += len(s) - one_count
        
        temp1 = '1'*one_count
        
        # bin변환
        s = bin(one_count)[2:]
        # print(convert_count)
        convert_count+=1
  
    return [convert_count,zero_count]