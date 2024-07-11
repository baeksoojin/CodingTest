n,s = map(int, input().split())

n_list = list(map(int, input().split()))

prefix_sum = [0]*(n)
prefix_sum[0] = n_list[0]
for i in range(1,n):
    prefix_sum[i] = prefix_sum[i-1] + n_list[i]
prefix_sum = [0] + prefix_sum

# two pointer

left, right, current_sum = 0, 0, 0
min_len = 10e9

while right <= n:

    current_sum = prefix_sum[right] - prefix_sum[left]
    
    if current_sum >= s:
        min_len = min(right-left, min_len)
        left+=1
    else:
        right+=1
        

    
if min_len == 10e9:
    print(0)
else:
    print(min_len)