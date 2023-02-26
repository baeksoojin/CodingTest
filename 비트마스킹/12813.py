'''
이진수 연산

두 이진수의 길이는 모두 100000임.

2^100000-1까지의 수를 가짐

길이를 입력받고 

'''


a= int(input(),2)
b= int(input(),2)

n = 100000
mask = 2**n-1
# print(a)
# print(b)

print(bin(a&b)[2:].zfill(n))
print(bin(a|b)[2:].zfill(n))
print(bin(a^b)[2:].zfill(n))
print(bin(mask^a)[2:].zfill(n))
print(bin(mask^b)[2:].zfill(n))