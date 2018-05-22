# FileName : main.py
# Author   : Adil
# DateTime : 2018/2/1 12:00
# SoftWare : PyCharm

import sys
from TEST.test2 import Ui_MainWindow
from TEST.testchild import Ui_Frame
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget

class windows(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(windows,self).__init__()
        self.setupUi(self)
 #       self.addWinAction.triggered.connect(self.child)

 #   def childshow(self):
  #      sel

class child(QWidget,Ui_Frame):
    def __init__(self):
        super(child,self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui=windows()
#    ui = child()
    ui.show()
    sys.exit(app.exec_())