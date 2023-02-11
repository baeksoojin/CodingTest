# Join type 정리

> join은 같은 값을 가지는 컬럼으로 서로 다른 테이블을 합치는 것을 의미한다.<br>

## inner join

- 사용 목적

    두 테이블의 내용이 모두 필요할때 사용한다. tableA , tableB가 있을 때 tableA의 column과 tableB의 column이 모두 필요하다면 inner join을 사용한다.

- 구문 정리
    
    `select [열 목록] from [첫번째 테이블] join [두번째 테이블] on [조인조건] where [검색조건]`<br>

    
    