def solution(answers):
    answer = []
    
    answer1 = [1,2,3,4,5]
    answer2 = [ 2, 1, 2, 3, 2, 4, 2, 5]
    answer3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    count1 = count2 = count3 = 0
    
    for i in range(len(answers)):
        if answers[i] == answer1[i%len(answer1)]:
            count1 +=1
        if answers[i] == answer2[i%len(answer2)]:
            count2 +=1
        if answers[i] == answer3[i%len(answer3)]:
            count3 +=1
            
    max_count = max([count1,count2, count3])
    index = 1
    for count in [count1,count2, count3]:
        if count == max_count:
            answer.append(index)
        index+=1
    
    
    return answer