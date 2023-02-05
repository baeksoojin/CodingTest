'''
1시 54분 시작

count[4] = min(count[4-1], count[4%2])


count[0]*(n+1)을 했을 때 런타임에러 -> 10*6+1로 미리 모든 경우를 고려해서 할당받으면 런타임에러가 나지 않음.! 스터디때 공유하기.
와ㅇ이...??

'''

n = int(input())

# count = [0]*(n+1) #런타임에러
count = [0]*(10**6+1)
count[1]=0
count[2]=1
count[3]=1

for i in range(4,n+1):
    # 1을 뺀 값이 최소가 될 수 있기에 이후에 비교
    count[i] = count[i-1]+ 1

    if i%3==0:
        count[i] = min(count[i], count[i//3]+1)
    
    if i%2==0:
        count[i] = min(count[i], count[i//2]+1)

    # 1을 뺀 값과 3 혹은 2로 나눈 경우 모두를 고려하게 코드를 짜야함.

print(count[n])
