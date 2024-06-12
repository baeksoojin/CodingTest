
n,m= map(int,input().split())

n_list = list(map(int, input().split()))

s,e,result= 0,0,0 # 동일위치에서 시작
count=0

while s<n:

    # 부분합이 m보다 크다 -> s를 옮기기 +1
    if result > m:
        result -= n_list[s]
        s+=1
    else:
        if e >= n:
            break
        result += n_list[e]
        e+=1
    
    if result == m:
        count+=1

print(count)
    