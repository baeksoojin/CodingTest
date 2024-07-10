'''
곱하거나 더할 것을 처리하기 위한 로직을 모르겠음.
-> ()[] 이렇게 나온 경우에는 )전체 stack에 )가 담겨있음 -> *2 
만약 ([]) 이경우에는 ] 전에 (, [가 둘다 있음 -> *3*2
만약 ([][])이 경우에는 answer에 2곱하기를 [] + []에 둘다 해줘야함. 2를 곱한 거를 계속 )를 만나기 전까지 유지해야함.
=> 해당 부분이 중요했음 ]가 나오면 +를 해줘야하고 둘러싼 괄호가 있다면 그 안에 있는 것들에 모두 분배법칙.
-> (가 나오면 *를 적용 , )가 나오면 +를 적용하고 현재 괄호에 맞는 값을 나눠줌. -> 그러면 *영역을 나눌 수 있음.
'''

input_string  = input()
result = 0
multi = 1
stack = []

flag = True


for i in range(len(input_string)):

    current = input_string[i]

    # ( -> *2
    if current == "(":

        stack.append("(")
        multi *= 2

    elif current == "[":

        stack.append("[")
        multi *=3
    elif current == ")":

        if len(stack)==0 or stack[-1]!="(":
            flag = False
            break
        if input_string[i-1] == "(": # 바로 직전 값이 )일때
            result += multi
        multi = multi//2
        stack.pop()
    else:
        
        if len(stack) == 0 or stack[-1]!="[":
            flag= False
            break
        if input_string[i-1] == "[": # 바로 직전 값이 )일때
            result += multi
        multi = multi//3
        stack.pop()
    
if len(stack) !=0 or flag==False:
    print("0")
else:
    print(result)
    





