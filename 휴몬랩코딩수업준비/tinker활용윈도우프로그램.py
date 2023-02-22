
# 1
# from tkinter import *
# root = Tk() # root window는 다른 위젯보다 먼저 생성
# root.geometry("1000x200") #가로와 세로의 크기를 차례로 입력
# root.mainloop()

#2

# from tkinter import *
# root = Tk() # root window는 다른 위젯보다 먼저 생성
# root.geometry("1000x200") #가로와 세로의 크기를 차례로 입력
# root.title("배치")
# btn1 = Button(root, text="버튼배치1")
# btn2 = Button(root, text="버튼배치2")

# btn1.pack(side=LEFT)
# btn2.pack(side=RIGHT)

# root.mainloop()

# 3
from tkinter import *
root = Tk() # root window는 다른 위젯보다 먼저 생성
root.geometry("1000x200") #가로와 세로의 크기를 차례로 입력
root.title("배치")
btn1 = Button(root, text="버튼배치1")
btn2 = Button(root, text="버튼배치2")
btn3 = Button(root, text="버튼배치3")

btn1.pack(side=LEFT, padx = 20)
btn2.pack(side=LEFT, padx = 20)
btn3.pack(side=LEFT, padx = 50)

root.mainloop()

# 4. 신입사원정보를 입력받을 수 있는 테이블을 생성해보자. -> 209페이지 따라하기

# 랜덤하게 추천하여 수업학생들의 이름을 띄워주고 리셋버튼을 누르면 이름을 지우는 위젯을 만들어보자!