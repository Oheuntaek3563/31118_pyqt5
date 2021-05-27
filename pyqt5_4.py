import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont

""" pyqt5 툴팁 나타내기"""

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10)) # 툴팁에 사용될 폰트를 설정, 10px크기와 SansSerif폰트를 사용 
        self.setToolTip('This is a <b>QWidget</b> widget 툴팁 표시') # setToolTip()을 사용, 표시될 텍스트를 입력

        btn = QPushButton('버튼', self) 
        btn.setToolTip('This is a <b>QPushButton</b> widget 이것은 버튼입니다.') # 버튼에 툴팁을 달아줌
        btn.move(50, 50)
        btn.resize(btn.sizeHint())

        self.setWindowTitle('Tooltips')
        self.setGeometry(300, 300, 300, 200)
        self.show()

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())