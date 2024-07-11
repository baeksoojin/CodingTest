n, s = map(int, input().split())
n_list = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + n_list[i - 1]

# Two pointer
left, right, min_len = 0, 1, float('inf')

while right <= n:
    current_sum = prefix_sum[right] - prefix_sum[left]

    if current_sum >= s:
        min_len = min(min_len, right - left)
        left += 1
    else:
        right += 1

if min_len == float('inf'):
    print(0)
else:
    print(min_len)
