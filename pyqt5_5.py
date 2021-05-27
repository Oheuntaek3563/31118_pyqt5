import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

""" 상태바 표시 """

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('※공부중~~') # showMessage()를 사용, 상태바에 표시될 메세지 설정 | QMainWindow클래스의 statusbar로 상태바 생성 
        
        self.setWindowTitle('Statusbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())   