## BOJ 동적프로그래밍 오답정리
---

### 평범한 배낭 [12865]
[요약] : 물건의 무게가 최대 K까지 가능할 때 만들 수 있는 배낭의 가치 V가 최대가 가능한 경우, 그 가치를 출력하는 문제<br>
물품의 개수 N과 버틸 수 있는 무게 K 가 주어진다. 두번째 줄부터 W, V가 주어진다.

1. 최댓값을 뽑아내야하기에, 물건의 가치를 담는 list를 모두 0로 초기화하고 시작한다.
2. N줄에 걸쳐서 입력받은 N개의 물건에 대한 무게와 가치를 tuple로 넣고 for문을 돌면서 최댓값을 갱신한다.

[틀렸던 이유]<br>
최댓값을 저장하는 결과 list를 일차원 배열로 갱신하는 코드를 작성했었음<br>
~~~
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

result = [0]*(m+1)
bags = []

for i in range(n):
    a,b = map(int,input().split())
    bags.append((a,b))

for bag in bags:
    for i in range(bag[0], m+1):
        result[i] = max(result[i],bag[1]+result[i-bag[0]])
    print(result)

# print(result)
print(max(result))
~~~

만약에 input값이 아래와 같이 들어간다고 해보자!<br>
```
3 6
3 4
3 5
6 5
```
결과는 
~~~
[0, 0, 0, 4, 4, 4, 8]
[0, 0, 0, 5, 5, 5, 10]
[0, 0, 0, 5, 5, 5, 10]
10
~~~
다음과 같이 나와서 틀린 답이 된다.<br>
배낭은 한번만 사용할 수 있기 때문이다. 그렇다면 (3,5)를 두번 사용하는 것이 아닌 (3,4), (3,5)를 사용해야한다.<br>
따라서 value의 결과를 담는 result list를 이차원 행렬로 구현해서 이전에 담긴 list를 사용해야할 것이다.
<br>

[해결코드]
~~~
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

result = [[0]*(m+1) for _ in range(n+1)] # 2차원 랭렬로 변경
bags = [(0,0)] # for문을 돌릴 때 1부터 Index를 사용

for i in range(n):
    a,b = map(int,input().split())
    bags.append((a,b))

for i in range(1,n+1):
    for j in range(1,m+1):
        if bags[i][0]>j:
            result[i][j] = result[i-1][j]
        else:
            result[i][j] = max(result[i-1][j], bags[i][1]+ result[i-1][j-bags[i][0]])
        

print(result[n][m])
~~~

```
#input
3 6
3 4
3 5
6 5
#result
[[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 3, 3, 3, 3], [0, 0, 0, 3, 3, 3, 6], [0, 0, 0, 3, 3, 3, 6]]
```
<br>
backjoon 숏코딩 풀이 중 다른 풀이를 참고해보니 더 간결하게 작성하는 방법이 있었.<br>

```
m=lambda:map(int,input().split())
n,k=m()
c=[0]*(k+1)
for i in range(n):
    w,v=m()
    c=[c[j] if w>j else max(c[j-w]+v,c[j]) for j in range(k+1)]
print(c[-1])
```
다음과 같이 작성한다면 첫 코드를 최대한 유지하면서 작성할 수 있었다. <br>
오답을 내지 않는 이유는 for문이 다 돌고나서 cost값이 저장되는 c list가 초기화되기 때문이다.<br>
처음에는 배열의 값이 초기화되면 이전 값이 날라가서 처음에 짠 코드와 동일하지 않을까?했지만 정답으로 나와있어서 그럴 수는 없었다,,,ㅎㅎ<br>
그래서 디버깅을 해보니, for문을 다 돌고나서 c[j]에 담겨져있는 것들이 모두 c=[~~~]로 인해서 갱신된다는 것을 알게 되었다.<br>
이차원 배열이 아닌 위와 같이 배열 초기화를 미루는 방식으로 코드를 작성해도 고민했던 문제를 해결할 수 있다는 것을 알게 되었다 :)
