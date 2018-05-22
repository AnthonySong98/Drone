from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

global sec
sec=0

class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget,self).__init__()
        self.setWindowTitle('thread例子')
        self.bst=QPushButton('开始',self)
        layout=QGridLayout()
        self.scd = QLCDNumber()
        layout.addWidget(self.scd,0,0,1,2)
        layout.addWidget(self.bst, 1,0,1,2)
        self.setLayout(layout)
        self.thread1=Thread()
        self.timer=QTimer()
        self.bst.clicked.connect(self.count)
        self.timer.timeout.connect(self.display)

    def count(self):
        self.timer.start(1000)
        self.thread1.start()
        self.thread1.sinOut.connect(self.end)

    def end(self):
        self.timer.stop()
        global sec
        print('结束用时:',sec)
        sec=0

    def display(self):
        global sec
        sec=sec+1
        self.scd.display(sec)

class Thread(QThread):
    sinOut=pyqtSignal()

    def __init__(self):
        super(Thread,self).__init__()
        print (1)

    def run(self):
        print(2)
        for i in range(200000000):
            pass
        self.sinOut.emit()
        print(3)

if __name__=='__main__':
    app=QApplication(sys.argv)
    icon=MainWidget()
    icon.show()
    sys.exit(app.exec_())

