def solution(book_time):
    answer = 0
    
    # 시작시간을 기준으로 정렬하기. 모든 방을 돌면서  end값보다 다음의 start값이 더 이전이라면 새로운 방을 배정해야함.
    # start값을 담을 변수가 필요함.
    # 이때 end값에서 +10을 해줘야함.
    
    # 입장과 청소를 마치는 시간을 int값으로 변경
    book_time_min = []
    
    for time in book_time:
        start_temp = time[0].split(":")
        start = int(start_temp[0])*60+int(start_temp[1])
        end_temp = time[1].split(":")
        end = int(end_temp[0])*60+int(end_temp[1])+10
        
        # print(start, end)
        book_time_min.append([start, end])
        
    
    
    # 로직작성
    
    rooms = []
    
    book_time_min.sort()
    for i in range(len(book_time_min)):
        if i==0:
            rooms.append(book_time_min[i])
        else:
            
            start_temp = book_time_min[i][0]
            flag = 0
            
            for j in range(len(rooms)):
                if start_temp>=rooms[j][1]:
                    # 다른 호텔방을 예약하지 않아도됨.
                    rooms[j] = book_time_min[i]
                    flag = 1
                    break
                    
                    
            # 다른호텔방을 예약해야하는 경우
            if flag==0:
                rooms.append(book_time_min[i])
                
                
        
        # print(rooms)
        answer = len(rooms)
    
        
        
        
    
    return answer