array = list(input().strip())
stack = []
plus_len, k_value = 0, 0
for s in array :
    if s == "(" :
        stack.append((plus_len - 1, k_value))
        plus_len = 0
    elif s == ")" :
        current_plus_len, current_multi_value = stack.pop()

        plus_len = plus_len * current_multi_value + current_plus_len
    else :
        plus_len += 1
        k_value = int(s)

print(plus_len)