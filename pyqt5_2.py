import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

""" pyqt5 어플리케이션 아이콘 삽입하기"""

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Icon') 
        self.setWindowIcon(QIcon('web.png')) # setWindowIcon()을 사용 : 어플리케이션 아이콘을 설정함. 
        self.setGeometry(300, 300, 300, 200) # setGeometry()을 사용 : 창의 위치와 크기를 설정. 
        """ 첫번째와 두번째는 x,y의 위치를 지정, 세번째와 네번째는 창의 너비와 높이를 결정 """
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())