import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication

""" pyqt5 창닫기 버튼 """

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('close', self) # QPushButton 'close'라는 푸시버튼을 생성
        btn.move(50, 50)
        btn.resize(btn.sizeHint()) 
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('Quit Button') 
        self.setGeometry(300, 300, 300, 200) 
        self.show()
 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())