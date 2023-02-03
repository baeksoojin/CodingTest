SELECT count(USER_ID) as USERS from USER_INFO where (JOINED like '2021%' ) and (20<=AGE and  AGE<=29);

'''
연산자는 쪼개서 작성해야함. <=AGE<=로 표현하면 틀림.
'''