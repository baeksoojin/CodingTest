h,w = map(int, input().split())

# 이차원 배열 생성
tile = [[0]*w for _ in range(h)]

h_list = list(map(int, input().split()))
for i in range(w): # w개 h가 주어진다.
    h_temp = h_list[i]
    for j in range(h_temp):
        tile[j][i] = 1

result = 0

for i in range(h):
    h_count = 0
    for j in range(w):
        count_temp=0
        if tile[i][j]==1:
            next = j+1
            while next<=w-1 and tile[i][next] ==0 :
                count_temp+=1
                next +=1
            if next-1 == w-1:
                  count_temp = 0  
                            
        h_count += count_temp

    result += h_count
print(result)