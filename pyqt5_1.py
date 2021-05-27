import sys
from PyQt5.QtWidgets import QApplication, QWidget

""" 오은택의 pyqt5 창 띄우기"""

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application') # setWindowTitle() : 타이틀바에 나타나는 창의 제목 설정
        self.move(300, 300) # move() : 위젯의 스크린의 위치를 x, y 위치를 정해 이동 시킴
        self.resize(400, 200) # resize() : 위젯의 크기를 너비와 높이를 정해서 조절함.
        self.show() # show() : 위젯을 스크린에 보여줌


if __name__ == '__main__':
   app = QApplication(sys.argv) #모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성
   ex = MyApp()
   sys.exit(app.exec_())