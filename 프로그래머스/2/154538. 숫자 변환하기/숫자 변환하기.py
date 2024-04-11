'''
dp를 사용
1부터 1000000까지 돌면서 3가지 경우에 대해서 min값을 저장
'''


def solution(x, y, n):
    answer = 0
    
    
    n_list = [-1]*(y+1)
    
    n_list[x]=0
    
    for i in range(x, y+1):
        if n_list[i] == -1:
            continue
        # +n의 경우
        if i+n<= y and ((n_list[i+n] > n_list[i]+1) or n_list[i+n] == -1):
            n_list[i+n] = n_list[i]+1
        if i*2<= y  and ((n_list[i*2] > n_list[i]+1) or n_list[i*2] == -1):
            n_list[i*2] = n_list[i]+1
        if i*3<= y  and ((n_list[i*3] > n_list[i]+1) or n_list[i*3] == -1):
            n_list[i*3] = n_list[i]+1
    
    return n_list[y]
