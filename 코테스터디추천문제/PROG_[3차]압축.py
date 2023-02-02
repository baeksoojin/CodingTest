def solution(msg):
    answer = []
    
    
    # 문자열의 앞에서부터 하나씩 단위를 키워가면서 없을 때까지 체크해야함.
    # k -> 있음 , ka  -> 없음 (ka를 다음 번호로 등록하여 list에 저장해서 이후에 또 사용해야함.)
    
    alpabat = ['A','B','C','D','E','F','G','H','I',
               'J','K','L','M','N','O','P','Q','R','S','T','U',"V",'W','X','Y','Z']
    i = 0
    while(i<len(msg)):
        index_start = i
        # print("start_index",index_start)
        find_alp =''
        not_find_alt = ''
        
        while(True):
            if msg[index_start:i+1] not in alpabat:
                not_find_alt = msg[index_start:i+1]
                break
            else:
                find_alp = msg[index_start:i+1]
                # print(find_alp)
                i+=1
                if i==len(msg):
                    break
                
        # print("find",find_alp, "not_find",not_find_alt)
        # find_alp의 index출력
        for j in range(len(alpabat)):
            if alpabat[j]==find_alp:
                answer.append(j+1)
                # print("next",i)
        # not find alp를 list에 넣기
        alpabat.append(not_find_alt)
        # print("put index",len(alpabat))

    # print(answer)        
    return answer


solution("TOBEORNOTTOBEORTOBEORNOT")


'''

문제 읽는 시간 포함 30분 안으로 풀기 목표

정확히 34분걸림 -> 4분 오바함.
문자열 다루기 더 연습하기...!

'''