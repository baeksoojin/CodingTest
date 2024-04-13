def solution(n):
    
    if n==1:
        return [[1]]
    
    num = x = y = 0
    dir_index = 0
    answer = [[0]* n for _ in range(n)]
    
    for i in range(n**2):
        
        num+=1
        answer[x][y] = num
        
        if dir_index == 0:
            y+=1
            if y+1==n or answer[x][y+1]!=0:
                dir_index = 1
        elif dir_index ==1:
            x+=1
            if x+1 == n or answer[x+1][y]!=0:
                dir_index = 2
        elif dir_index==2:
            y-=1
            if y-1==-1 or answer[x][y-1]!=0:
                dir_index = 3
        else:
            x-=1
            if x-1==-1 or answer[x-1][y]!=0:
                dir_index=0
                

    return answer