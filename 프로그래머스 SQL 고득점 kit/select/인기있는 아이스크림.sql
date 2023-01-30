SELECT FLAVOR FROM FIRST_HALF ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID ASC;

'''
정렬기준이 2개 이상일때 먼저 고려해야하는 것을 왼쪽에 적어준다.ADD
내림차순 정렬일때 desc, 오름차순 정렬일때 asc를 사용한다. 다만 asc는 생략가능하다.

<정리>
select ~~ from ~~ oreder by ~~ [desc, asc];

'''