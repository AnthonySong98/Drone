import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class dialogDemo(QMainWindow):
    def __init__(self):
        super(dialogDemo,self).__init__()
        self.setWindowTitle('Dialogh')
        self.resize(300,400)

#        self.btn=QPushButton('弹出对话框',self)
#        self.btn.setText('弹出对话框')
#        self.btn.move(50,50)
#        self.btn.clicked.connect(self.showdialog)

        self.btn1=QPushButton('弹出对话框')
#        self.btn1.setChecked(True)
#        self.btn1.toggle()
#        self.btn1.move(90,90)


        layout=QVBoxLayout()
        layout.addWidget(self.btn1)
        self.setLayout(layout)

    def showdialog(self):
        diag=QDialog()
        btn=QPushButton('ok',diag)
        btn.move(50,50)
        diag.setWindowTitle('弹窗框1')
        diag.setWindowModality(Qt.WindowModal)
        diag.exec_()

if __name__=='__main__':
    app=QApplication(sys.argv)
    icon=dialogDemo()
    icon.show()
    sys.exit(app.exec_())

