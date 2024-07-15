
str = input()


b_len = str.count('b')
str = str+str

min_count = 10e9
for i in range(0,len(str)-b_len):
    # b의 묶음으로 만드는 경우
    min_count = min(min_count,str[i:i+b_len].count('a'))

print(min_count)