# 배열을 만들고 1부터 체크해서 연산량을 저장하면서 이후에 써먹기

count = [0]*30001

n = int(input())

for i in range(2,n+1):

    temp = count[i-1] + 1 # 각 경우와 비교해서 적은 결과가 나오는 것으로 채택

    if i==2:
        count[i] = temp
    elif i%5==0:
        count[i] = min(temp,count[i//5]+1)
    elif i%3==0:
        count[i] = min(temp,count[i//3]+1)
    elif i%2==0:
        count[i] = min(temp,count[i//2]+1)
    else:
        count[i] = temp

print(count[n])