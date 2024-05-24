def solution(n, lost, reserve):
    answer = 0
    
    
    # 잂어버린 사람 lost, reserve 여벌
    # 잃어버린 사람이 앞사람에게 여벌이 있다면
    
    # 앞사람에게 빌려주든 뒷사람에게 빌려주든 결과가 바뀌지 않음.
    
    cloth = set(reserve) - set(lost) # 여벌이 남아있는 옷을 가지고 있는 학생
    lost = set(lost) - set(reserve) # 잃어버린사람중 여벌이 있다면 그 사람은빌리지 않아도됨

    cloth_list = list(cloth)
    lost_list = list(lost)
    count =0
    
    for i in lost:
        if i-1 in set(cloth_list):
            # 여벌의 옷을 빌리기
            cloth_list.remove(i-1)
            count+=1
            continue
        if i+1 in set(cloth_list):
            cloth_list.remove(i+1)
            count+=1
        
    return n - (len(lost) - count)
    