'''
스택을 사용해야함.

스택이 비었을 경우 -> 저장
스택에 들어있을 경우 ->
1. 스택의 가장 마지막 값보다 현재 값이 큰 경우 -> 더 큰 것을 찾을 때까지 pop
2. 스택의 가장 마지막 값보다 현재 값이 작은 경우 -> 스택에 저장
'''


n = int(input())

n_list = list(map(int, input().split()))

stack = []

for i in range(len(n_list)):

    # 1. stack이 비어있을 경우
    if len(stack)==0:
        print("0", end= " ")
        stack.append(i)
    else:
        # 2-1. 가장 마지막 값이 현재보다 큰 경우
        if n_list[stack[-1]] > n_list[i]:
            print(stack[-1]+1, end = " ")
        else: # 2-2. 가장 마지막 값이 현재보다 작은 경우
            flag = False
            while(stack): # 스택에 값이 존재할 때까지
                current = stack[-1]
                if n_list[current] < n_list[i]: # 현재값보다 작다면 pop
                    stack.pop(len(stack)-1)
                else: # 현재보다 큰게 있다면 그것을 출력
                    print(current+1, end =" ")
                    flag = True
                    break

            if flag == False:# 수신할 수 없음
                print("0", end = " ")
            
            
        stack.append(i)
                

            
            
            

    