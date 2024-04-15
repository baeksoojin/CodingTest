'''
영어 끝말잇기
12시 33분 시작


cnt -> 총 횟수 -> 몇번재 사람인지 ? 총 횟수를 사람수로 나눈 나머지 -> 만약 4에서 걸렸다면? (4-1)%(사람이 3일때) -> 0 -> (0+1)1번째 사람
'''


def solution(n, words):


    cnt=1
    
    idx = 0
    before = words[idx]
    idx += 1
    
    before_set = set()
    before_set.add(before)
    
    flag = True
    while idx <= len(words)-1:
        
        current = words[idx]
        # idx ++
        idx +=1
        # before의 마지막 단어와 현재 앞 단어가 다를 때 -> break / 같다면 cnt++
        if before[-1]!=current[0] or current in before_set:
            flag = False
            break
        
        before = current
        before_set.add(current)
    
    
    if flag:
        return([0,0])
    else:
        if idx%n == 0:
            num = n
        else:
            num = idx%n
        if (idx)%(n)== 0:
            count = idx//n
        else:
            count = idx//n+1
            
        return [num,count]
            
            