'''
1시 58분 시작 -> 30분 제한시간
1시 16분 끝 -> 문자를 숫자로 변환할때는 ord를 사용하고 숫자를 문자로 변환할때는 chr를 사용한다.
'''

def solution(s, skip, index):
    
    answer = ''
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    for s_temp in s:
        current = ord(s_temp) - 97
        print(alphabet[current])
        count =0
        
        while(True):
            current+=1
            if alphabet[current%26] not in skip:
                count+=1
                
            if count==index:
                break
                
        answer += alphabet[current%26]
    return answer