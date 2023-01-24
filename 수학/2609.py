'''
최대공약수와 최소공배수를 구하기

최대공약수 => 유클리드 호제법을 활용
최소공배수 => 최대공약수를 사용해서 구할 수 있음

'''

# a,b = map(int,input().split())
# a_temp,b_temp = a,b

# if a<b : a,b = b,a

# while(b):
#     a,b = b, a%b

# print(a)

# print((a_temp//a) * (b_temp//a) * a )


'''
python package 존재

greates common divisor, least common multiple
'''
from math import gcd 

a,b = map(int,input().split())
print(gcd(a,b))
print(a*b//gcd(a,b))

#다만 시간이 더 올래걸렸음, 메모리차지도 더 많이함.



