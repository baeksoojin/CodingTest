'''
queue를 사용해서 하나씩 pop하고 그 수 뒤에서부터 체크하면 되는데,,,그냥 index범위 조절하면 같은 효과이지 않나?
굳이 queue를 사용하지 않아도될듯.?
'''
def solution(prices):
    
    answer = []
    
    for i in range(len(prices)-1):
        count = 0
        for j in range(i+1, len(prices)):
            count+=1
            if prices[j] - prices[i]<0:
                break
        answer.append(count)

    answer.append(0) # 가장 마지막은 항상 0
    return answer