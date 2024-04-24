def solution(answers):
    answer = []
    
    one_answer_list = [1,2,3,4,5]
    two_answer_list = [2, 1, 2, 3, 2, 4, 2, 5]
    three_answer_list = [ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    correct1 = correct2 = correct3 = 0
    
    for i in range(len(answers)):
        if answers[i] == one_answer_list[i%len(one_answer_list)]:
            correct1+=1
        if answers[i] == two_answer_list[i%len(two_answer_list)]:
            correct2+=1
        if answers[i] == three_answer_list[i%len(three_answer_list)]:
            correct3+=1
            
    values = [correct1, correct2, correct3]
    max_value = max(values)
    
    for i in range(3):
        if max_value == values[i]:
            answer.append(i+1)
    
    return answer