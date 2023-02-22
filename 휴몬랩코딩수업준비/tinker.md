# 위젯

> 네이버 사전 기준, 위젯의 의미는 PC, 휴대폰, 블로그·카페 등에서 웹브라우저를 통하지 않고 날씨·달력·계산기 등의 기능과 뉴스·게임·주식정보 등을 바로 이용할 수 있도록 만든 미니 응용프로그램이다.

tinker를 활용해 다양한 프로그램을 작성할 수 있다.<br>

## 기본 수행 문장들을 통한 빈 다이얼로그 출력

```
from tkinter import *
root = Tk() # root window는 다른 위젯보다 먼저 생성
root.geometry("1000x200") #가로와 세로의 크기를 차례로 입력
root.mainloop() # event 처리 루프를 돌기 시작함
```

## 위젯 배치와 크기 조정
pack()을 활용한다.<br>
- side를 활용한 정렬<br>

    ```
    btn1 = Button(root,text="버튼배치1")
    btn1.pack(side=LEFT)
    ```

    <img width="1000" alt="image" src="https://user-images.githubusercontent.com/74058047/220698523-ff45e3e5-bc29-4cc3-aeb0-24b5521de877.png">


- pad로 폭 조정하기

    pad : 여백조절<br> pack()함수에서 padx = 픽셀값 혹은 pady = 픽셀값으로 설정함으로써 여백 조절이 가능하다.

    ```
    btn1.pack(side=LEFT, padx = 20)
    btn2.pack(side=LEFT, padx = 20)
    btn3.pack(side=LEFT, padx = 50)
    ```

    <img width="985" alt="image" src="https://user-images.githubusercontent.com/74058047/220699410-89d4ed5e-76bc-4588-a098-c30a230f68c0.png">

    place로 절대 좌표를 통해 배치한다.<br>
    위젯.place(x,y,width,height)<br>
    grid로 지정된 row,column위에 위젯을 배치한다.<br>
    위젯.grid(row,column)<br>

