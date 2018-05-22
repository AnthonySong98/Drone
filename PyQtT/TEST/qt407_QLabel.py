from PyQt5.QtWidgets import *
import sys


class QlableDemo(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QLable例子')
        namel1=QLabel('&Name',self)
        nameEd1=QLineEdit(self)
        namel1.setBuddy(nameEd1)  #设置快捷键

        namel2 = QLabel('&Password', self)
        nameEd2 = QLineEdit()
        namel2.setBuddy(nameEd2)  # 设置快捷键

        btnOK=QPushButton('&Ok')
        btnCancel=QPushButton('&Cancel')

        #添加控件
        mainlayout=QGridLayout(self)
        mainlayout.addWidget(namel1,0,0)
        mainlayout.addWidget(nameEd1, 0, 1,1,2)
        mainlayout.addWidget(namel2,1,0)
        mainlayout.addWidget(nameEd2, 1, 1,1,2)
        mainlayout.addWidget(btnOK,2,1)
        mainlayout.addWidget(btnCancel, 2,2)
        self.setLayout(mainlayout)

if __name__=='__main__':
    app=QApplication(sys.argv)
    icon=QlableDemo()
    icon.show()
    sys.exit(app.exec_())

